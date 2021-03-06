def aufgabe1():
    satz = "Die Sonne ist ein Stern und die Planten kreisen um die Sonne."
    satz_liste = satz.lower().strip(".").split(" ")
    print(satz_liste)
    satz_dict = {word: satz_liste.count(word) for word in set(satz_liste)}
    print(satz_dict)
    n_satz = satz.replace(".", "!")
    print(n_satz)
    n_satz = n_satz.replace("und", "und ist ca. 4.6Mrd. Jahre alt")
    print(n_satz)


def aufgabe2():
    lange_liste = [[y for y in range(1, x)] for x in range(
        1, 10+2)]  # 10+2 wegen (1,10) => 1 bis 9
    print(lange_liste)

    noch_laenger_liste = []
    for liste in lange_liste:
        noch_laenger_liste.extend(liste)
    print(noch_laenger_liste)


def aufgabe3():
    hauptstadt_namen = {
        "Deutschland": "Berlin",
        "Frankreich": "Paris",
        "England": "London",
        "Spanien": "Madrid",
        "Niederland": "Amsterdam"
    }
    for land in hauptstadt_namen:
        print("Land:", land, "\tHauptstadt:", hauptstadt_namen[land])

    for key, value in hauptstadt_namen.items():
        print(key, value)

    key_liste = [key for key in hauptstadt_namen.keys()]
    print(sorted(key_liste, reverse=True))
    print(sorted(key_liste))


def main():
    aufgabe1()
    aufgabe2()
    aufgabe3()


if __name__ == "__main__":
    main()
