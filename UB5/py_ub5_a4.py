from mydatenbank_a4 import MyDatenbank
from py_ub5_a2 import returnSortierteNamen

def main():
    sortierte_namens_liste = returnSortierteNamen()
    print(sortierte_namens_liste)
    
    dbInst = MyDatenbank("UB5/Files/uebungsblatt5.db", "Aufgabe3")
    dbInst.connect()
    dbInst.generateTable()
    for i in range(len(sortierte_namens_liste)):
        dbInst.schreibeInTabelle(i, sortierte_namens_liste[i])
    dbInst.leseVonTabelle()

if __name__ == "__main__":
    main()

