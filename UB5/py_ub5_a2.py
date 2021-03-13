
def einlesen():
    string = ""
    with open("namen.txt","r") as txtfile:
        string += txtfile.read()
    string = string.strip()
    namens_liste = string.split("\n")
    return namens_liste

def sortierenNachNachnamen(namens_liste):
    namens_liste.sort(key = lambda a: a.split(" ")[1])
    return namens_liste

def writeInTxt(sortierte_namensListe):
    with open("namen.txt", "w") as txtfile:
        txtfile.write("")
        for name in sortierte_namensListe:
            txtfile.write(name + "\n")

def returnSortierteNamen():
    namens_liste = einlesen()
    sortierte_namens_liste = sortierenNachNachnamen(namens_liste)
    print(sortierte_namens_liste)
    return sortierte_namens_liste  

def main():
    sortierte_namensListe = returnSortierteNamen()
    writeInTxt(sortierte_namensListe)

if __name__ == "__main__":
    main()