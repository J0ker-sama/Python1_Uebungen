from mydatenbank_a7 import MyDatenbank


def main():
    dbInst = MyDatenbank("UB5/Files/uebungsblatt5.db", "Aufgabe7")
    dbInst.connect()
    dbInst.leseVonTabelle()
    dbInst.dbInCsv()

if __name__ == "__main__":
    main()