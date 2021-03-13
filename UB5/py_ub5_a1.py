from primzahlen_generator import returnPrimzahlenListe


def main():
    primezahl_bis = 1000
    with open("py_ub5_a1_primenzahlen.txt","w") as txtfile:
        # erste einzelne Zahlen in Liste zu einer str machen durch map-Funktion
        string = ",".join(map(str, returnPrimzahlenListe(primezahl_bis)))
        txtfile.write(string)

if __name__ == "__main__":
    main()