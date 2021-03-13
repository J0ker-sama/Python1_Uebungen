import datetime
import time
import pandas as pd
from primzahlen_generator import returnPrimzahlenListe
from mydatenbank_a5 import MyDatenbank





def main():
    dbInst = MyDatenbank("UB5/Files/uebungsblatt5.db", "Aufgabe5")
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
    