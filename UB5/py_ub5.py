# Aufgabe 1)
import gzip
import shutil


def aufgabe1(bisZahl):
    def allePrimzahlenAll(bisZahl):
        primeZahlenListe = []
        for i in range(2, bisZahl+1):
            istTeiler = False
            for j in range(2, i):
                if (i % j == 0):
                    istTeiler = True
            if (istTeiler == False):
                primeZahlenListe.append(str(i))
        return primeZahlenListe

    def inFileSchreiben(primenZahlenListe):
        zeichenkette = ", ".join(primenZahlenListe)

        with open("./UB5/py_ub5_aufgabe1.txt", "w") as txt_file:
            txt_file.write(zeichenkette)
            txt_file.write("\n")
            txt_file.write("Laenge: {}".format(len(primenZahlenListe)))

    inFileSchreiben(allePrimzahlenAll(bisZahl))


def aufgabe2():
    with open("./UB5/py_ub5_aufgabe2.txt", "w") as txt_file:
        txt_file.write("Florian Luebbe\n")
        txt_file.write("Sven Birkenfeld\n")
        txt_file.write("Max Huesmann\n")
        txt_file.write("Jan Helfen\n")
        txt_file.write("Thelagsan Vigneswaran\n")
        txt_file.write("Nick Werner\n")
        txt_file.write("dssaDS asAS\n")
        txt_file.write("ass ASsSSa\n")
        txt_file.write("asDSAD ASasaS\n")
        txt_file.write("asdAS SDRWF\n")

    line_liste = []
    with open("./UB5/py_ub5_aufgabe2.txt", "r") as txt_file:
        for line in txt_file:
            # print(line.strip("\n"))
            line_liste.append(line.strip("\n"))
        print(line_liste)

    sortierte_Liste = line_liste.sort(key=lambda a: a[0])


def aufgabe3():
    with open("./UB5/py_ub5_aufgabe2.txt", "rb") as f_in:
        with gzip.open("./UB5/py_ub5_aufgabe2.txt.gz", "wb") as f_out:
            f_out.writelines(f_in)
            # shutil.copyfileobj(f_in, f_out)


def main():
    aufgabe1(1000)
    aufgabe2()
    aufgabe3()


if __name__ == "__main__":
    main()
