
def aufgabe1():
    meine_liste = ["Katze", "Hund", 17, "Super", 3.14]
    print(meine_liste)
    meine_liste[2] = 123
    print(meine_liste)
    print(len(meine_liste))
    meine_liste.append("Ni")
    print(meine_liste)
    meine_liste.extend([4, 5, 3.14])
    print(meine_liste)
    meine_liste.insert(2, "Taube")
    print(meine_liste.count(3.14))
    print(meine_liste.index(3.14))
    meine_liste.remove(3.14)
    print(meine_liste)
    meine_liste.pop()
    print(meine_liste)
    meine_liste.reverse()
    print(meine_liste)
    print(sum([1, 2, 3]))


def aufgabe2():
    liste_a = ["Hallo", "schönes", "Wetter"]
    liste_b = liste_a
    liste_b[1] = "schlechtes"
    print(liste_a[0], liste_a[1], liste_a[2])  # Hallo schlechtes Wetter
    # Referenz wird geändert -> auswirkung auf liste_a


def aufgabe3():
    L = ["Meier", "Bauer", "Moser", "Molitor", "Martin"]
    # Verarbeitung
    trifftzu = True
    for e in L:
        if e[0] != "M":
            trifftzu = False

    if trifftzu == True:
        print("Alle Namen fangen mit M an.")
    else:
        print("Nicht alle Namen fangen mit M an.")
    # Das Programm schaut, ob alle Namen in der Liste L mit dem Buchstaben "M" beginnt


def aufgabe4():
    xWerte = [-2, -1, 0, 0.5, 1, 1.5, 2]
    yWerte = []
    for x in xWerte:
        y = x*x - 4
        yWerte = yWerte + [y]  # ist das Gleiche wie: yWerte.append(y)
    print(xWerte)
    print(yWerte)


def aufgabe5():
    liste_100 = [x for x in range(0, 10)]
    print(liste_100)
    liste_100 = [ele*2 for ele in liste_100]
    print(liste_100)


def aufgabe6():
    namens_liste = ["Carl", "Matha", "Monika", "Hansi", "Peter", "Mia", "Maximus", "Metchild", "Klaus", "Carsten", "Mats", "Maurits", "Mette",
                    "Nils", "Jan", "Harald", "Simone", "Mette", "Martha"]
    print(namens_liste)
    namens_liste_M = [ele for ele in namens_liste if ele[0] == "M"]
    print(namens_liste_M)


def aufgabe7():
    def aufgabe71():
        L = [0, 1, 2, 3, 4, 5]
        M = L
        for i in range(len(M)):
            M[i] = M[i] + 1
        print(M)
        print(L)

    def aufgabe72():
        L = [0, 1, 2, 3, 4, 5]
        M = L[:]
        for i in range(len(M)):
            M[i] = M[i] + 1
        print(M)
        print(L)

    def aufgabe73():
        L = [1, 2, 3]
        print(L)
        H = L
        for i in range(len(L)):
            L[i] = H[len(L)-i-1]  # von hinten nach vorne in L
        print(L)

    print("Aufgabe71:")
    aufgabe71()
    print("Aufgabe72:")
    aufgabe72()
    print("Aufgabe73:")
    aufgabe73()


def main():
    aufgabe1()
    aufgabe2()
    aufgabe3()
    aufgabe4()
    aufgabe5()
    aufgabe6()
    aufgabe7()


if __name__ == "__main__":
    main()
