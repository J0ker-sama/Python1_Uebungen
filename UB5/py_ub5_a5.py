import sqlite3
import datetime
import time
import pandas as pd
from py_ub_a1 import returnPrimzahlenListe


class MyDatenbank(object):
    def __init__(self, datenbank_name, TabellenName):
        self.db_name = datenbank_name
        self.tab_name = TabellenName

    def connect(self):
        self.connect = sqlite3.connect(self.db_name)
        print("Erfolgreich verbunden!")

    def generateTable(self):
        query = "CREATE TABLE IF NOT EXISTS " + str(self.tab_name) + " (ID INT PRIMARY KEY NOT NULL, DATE TEXT NOT NULL, UNIX INT NOT NULL, PRIMZAHL INT NOT NULL);"
        self.connect.execute(query)

    def schreibeInTabelle(self, counter, uhrzeit, unixzeit, primzahl):
        query = "INSERT INTO " + str(self.tab_name) + " (ID, DATE, UNIX, PRIMZAHL) VALUES (" + str(counter) + ", \"" + str(uhrzeit) + "\" , \"" + str(unixzeit) + "\", \"" + str(primzahl) + "\");"
        self.connect.execute(query)
        self.connect.commit()
        print("Eintrag war erfolgreich und wird geschlossen.")

    def leseVonTabelle(self):
        query = "SELECT * FROM " + str(self.tab_name) + ";"
        answer = self.connect.execute(query)
        for row in answer:
            print(row)

    def tabelleInCSV(self):
        db_df = pd.read_sql_query("SELECT * FROM " + str(self.tab_name), self.connect)
        db_df.to_csv(str(self.tab_name) + ".csv", index=False)
        print(str(self.tab_name) + ".csv wurde erzeugt!")


def main():
    dbInst = MyDatenbank("uebungsaufgabe55.db", "Aufgabe5")
    dbInst.connect()
    dbInst.generateTable()
    primZahlenList = returnPrimzahlenListe(100)

    for i in range(10):
        uhrzeit = datetime.datetime.now()
        unixzeit = int(time.time())
        primzahl = primZahlenList[i]
        dbInst.schreibeInTabelle(i, uhrzeit, unixzeit, primzahl)
        time.sleep(2)
    dbInst.leseVonTabelle()
    dbInst.tabelleInCSV()

if __name__ == "__main__":
    main()
    