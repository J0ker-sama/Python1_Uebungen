
def returnPrimzahlenListe(bisZahlen):
    primZahlListe = []
    for i in range(2, bisZahlen+1):
        istTeiler = False
        for j in range(2, i):
            if(i % j == 0):
                istTeiler = True
                break
        if(istTeiler == False):
            primZahlListe.append(i)
    return primZahlListe
