
def aufgabe1(zeichenkette):
    print("Aufgabe1:")
    # zeichenkette = "[1,2,3,4, [a,b,c,d], help, run, [[a,b],[1,2]]]\n"
    # [1,2,3,4, [a,b,c,d], help, run, [[a,b],[1,2]]] -> Plus Leerzeile
    print(zeichenkette)
    # neu_liste = zeichenkette.split()

    # a)
    print("a)")
    zeichenkette = zeichenkette.strip("\n")
    # [1,2,3,4, [a,b,c,d], help, run, [[a,b],[1,2]]] -> Ohne Leerzeile
    print(zeichenkette)

    # b)
    print("b)")
    zeichenkette = zeichenkette[1:-1]
    print(zeichenkette)  # 1,2,3,4, [a,b,c,d], help, run, [[a,b],[1,2]]

    # c)
    print("c)")
    zeichenkette_liste = zeichenkette.split(", ")
    print(zeichenkette_liste)

    # d)
    print("Zeichen1:", int(zeichenkette_liste[0][4]))  # Zeichen1: 3
    print("Zeichen2:", int(zeichenkette_liste[-1][-3]))  # Zeichen2: 2
    ergebnis = int(zeichenkette_liste[0][4]) * \
        int(zeichenkette_liste[-1][-3])  # Ergebnis: 6
    print("Ergebnis:", ergebnis)
    # ['1,2,3,4', '[a,b,c,d]', 'help', 'run', '[[a,b],[1,2]]']
    # ['DONE', 'DONE', 'help', 'run', '[[a,b],[1,2]]']
    # ['DONE', 'DONE', 'DONE', 'DONE', [[[a,b]][[1,2]]']
    print(zeichenkette_liste)
    neue_zeichenkette_liste = []
    for ele in zeichenkette_liste:
        if "[" and "]" in ele:
            tempListe = []
            # for e in ele[1:-1]:
            tempListe = ele[1:-1].split(",")
            neue_zeichenkette_liste.append(tempListe)
        elif "," in ele:
            tempListe = []
            tempListe = ele.split(",")
            neue_zeichenkette_liste.append(tempListe)
            # neue_zeichenkette_liste.append(ele)
        else:
            neue_zeichenkette_liste.append(ele)
    print(neue_zeichenkette_liste)
    # [1,2,3,4, ['a','b','c','d'], "help", "run", [["a","b"],[1,2]]]


def aufgabe2(zeichenkette):
    # a)
    stripped_zeichenkette = zeichenkette.strip("\n")
    index_ab = stripped_zeichenkette.find("[a,b]")
    print(index_ab)  # 33

    # b)
    stripped_zeichenkette = stripped_zeichenkette.replace("2", str(1234))
    print(stripped_zeichenkette)


def aufgabe3():
    def rekursion(i):
        if i == 0:
            return 1
        elif i == 1:
            return 1
        return i*rekursion(i-2)

    dictionary = {i: rekursion(i) for i in range(20)}
    for key, value in dictionary.items():
        print(key, value)


def aufgabe4():
    from datetime import datetime
    import time
    for i in range(5):
        print(str(i) + ":", datetime.now().strftime("%d.%m.%Y, %H:%M:%S"))
        time.sleep(2)


def aufgabe5():
    from datetime import datetime
    import time
    old_date = datetime(1983, 3, 21, 22, 4, 56)
    for i in range(5):
        actual_date = datetime.now().replace(microsecond=0)
        difference_time = actual_date - old_date
        print(str(i) + ":", difference_time)
        time.sleep(5)


def aufgabe61(x):
    try:
        result = x / 2
        f = aufgabe62(result)
        return f
    except:
        return -1


def aufgabe62(x):
    try:
        result = x / 2
        f = aufgabe63(result)
        return f
    except:
        return -2


def aufgabe63(x):
    try:
        return x/0
    except:
        return -3


def main():
    # aus Aufgabe
    zeichenkette = "[1,2,3,4, [a,b,c,d], help, run, [[a,b],[1,2]]]\n"
    aufgabe1(zeichenkette)
    aufgabe2(zeichenkette)
    aufgabe3()
    aufgabe4()
    aufgabe5()
    e = aufgabe61(100)
    print(e)


if __name__ == "__main__":
    main()
