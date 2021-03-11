import sqlite3


class MyDatenbank(object):
    def __init__(self, datenbank_name, TabellenName):
        self.db_name = datenbank_name
        self.tab_name = TabellenName

    def connect(self):
        self.connect = sqlite3.connect(self.db_name)
        print("Erfolgreich verbunden!")

    def generateTable(self):
        query = "CREATE TABLE IF NOT EXISTS " + str(self.tab_name) + " (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL);"
        self.connect.execute(query)

    def schreibeInTabelle(self, counter, name):
        query = "INSERT INTO NamensTabelle (ID, NAME) VALUES (" + str(counter) + ", \"" + str(name) + "\" );"
        self.connect.execute(query)
        self.connect.commit()
        print("Eintrag war erfolgreich und wird geschlossen.")

    def leseVonTabelle(self):
        query = "SELECT * FROM NamensTabelle;"
        answer = self.connect.execute(query)
        for row in answer:
            print(row)


def main():
    dbInst = MyDatenbank("uebungsaufgabe5.db", "NamensTabelle")
    dbInst.connect()
    dbInst.generateTable()
    for i in range(10):
        string = "Python_ " + str(i)
        dbInst.schreibeInTabelle(i, string)
    dbInst.leseVonTabelle()

if __name__ == "__main__":
    main()

