
def createNamesFile():
    txtfile = open("namen.txt","w")
    namens_liste = [
        ("Hans","Mimo"),
        ("Zed", "Feuerstein"),
        ("Wald", "Duck"),
        ("Anro", "Wild")]

    for vorname, nachname in namens_liste:
        txtfile.write(vorname + " " + nachname + "\n")
    txtfile.close()


def main():
    createNamesFile()

if __name__ == "__main__":
    main()

