import sqlite3
import csv 

class MyDatenbank(object):
    def __init__(self, datenbank_name, TabellenName):
        self.db_name = datenbank_name
        self.tab_name = TabellenName

    def connect(self):
        self.connect = sqlite3.connect(self.db_name)
        print("Erfolgreich verbunden!")

    def generateTable(self):
        query = "CREATE TABLE IF NOT EXISTS " + str(self.tab_name) + " (ID INTEGER PRIMARY KEY AUTOINCREMENT, DATE TEXT NOT NULL, UNIX INT NOT NULL, PRIMZAHL INT NOT NULL, SENSOR TEXT NOT NULL);"
        self.connect.execute(query)

    def schreibeInTabelle(self, uhrzeit, unix, primzahl, sensor):
        query = "INSERT INTO " + str(self.tab_name) + " (DATE, UNIX, PRIMZAHL, SENSOR) VALUES (\"" + str(uhrzeit) + "\" , \"" + str(unix) + "\" , \"" + str(primzahl) + "\" , \""  + str(sensor) + "\" );"
        self.connect.execute(query)
        self.connect.commit()
        print("Eintrag war erfolgreich und wird geschlossen.")

    def leseVonTabelle(self):
        query = "SELECT * FROM " + str(self.tab_name) + ";"
        answer = self.connect.execute(query)
        for row in answer:
            print(row)

    # Aufgabe 7
    def dbInCsv(self):
        query = "SELECT * FROM " + str(self.tab_name) + ";"
        answer = self.connect.execute(query)
        with open("UB5/Files/dbInCSV-" + str(self.tab_name) + ".csv", "w", newline="") as csvFile:
            csvwriter = csv.writer(csvFile, delimiter = ";")
            for row in answer:
                csvwriter.writerow(row)
            