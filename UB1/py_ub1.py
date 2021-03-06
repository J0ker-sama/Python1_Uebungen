import random


def aufgabe1():
    print("Variablen swappen...")
    a, b = 3, 4
    print(a, b)
    a, b = b, a
    print(a, b)


def aufgabe2():
    print("Listen erstellen...")
    liste1 = [random.randint(0, 9) for i in range(0, 10)]
    liste2 = ["Hello", "World", "Programm", "Rekord", "Hochschule",
              "Bochum", "Fussball", "Alkohol", "Zigarretten", "Florian", "Philipp"]
    liste3 = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.uniform(
        1.5, 4.5), random.uniform(1.5, 4.5), random.uniform(1.5, 4.5), random.uniform(1.5, 4.5), "abs", "dft", "etf"]
    print(liste1)
    print(liste2)
    print(liste3)
    return liste1, liste2, liste3


def aufgabe3():
    print("Listen sortieren...")
    liste1, liste2, liste3 = aufgabe2()
    print("Aufsteigend...")
    print(sorted(liste1))
    print(sorted(liste2))
    try:
        print(sorted(liste3))
    except Exception:
        print("Operation an Liste3 unmöglich!")
    print("Absteigend...")
    print(sorted(liste1, reverse=True))
    print(sorted(liste2, reverse=True))
    try:
        print(sorted(liste3, reverse=True))
    except Exception:
        print("Operation an Liste3 unmöglich!")
    print("Listenelement an Position 5 einfügen...")
    liste1.insert(5, random.randint(0, 9))
    liste2.insert(5, "Reus")
    try:
        liste3.insert(5, 2.3)
    except Exception:
        print("Operation an Liste3 unmöglich!")
    print(liste1)
    print(liste2)
    print(liste3)
    print("Listenelement an Position 2 löschen...")
    liste1.pop(2)
    liste2.pop(2)
    liste3.pop(2)
    print(liste1)
    print(liste2)
    print(liste3)
    print("Listenelement anderes Typs an Position 6 einfügen...")
    liste1.insert(6, "Florian")
    liste2.insert(6,6)
    liste3.insert(6,"sds")
    print("Nochmal sortieren...")
    try:
        print(sorted(liste1))
        print(sorted(liste2))
        print(sorted(liste3))
    except Exception:
        print("Operationen unmöglich!")

def main():
    print("Start UB1 ->")
    # aufgabe1()
    # aufgabe1() kann auskommentiert werden, da in aufgabe2() bereits aufgerufen!
    aufgabe2()
    aufgabe3()
    print("<- Ende UB1")

if __name__ == "__main__":
    main()

