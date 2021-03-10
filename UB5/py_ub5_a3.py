import gzip
import pickle


class MyGzip(object):

    def __init__(self, dateinname):
        self.dateiname = dateinname

    def zip_read(self):
        # leist zuerst einen Byte-Strom im Binary Format ein
        with gzip.open(self.dateiname, "rb") as dh:
            # mit der str() Funktion und "utf-8" Parameter, wird der Bytestrom in einen string konvertiert
            self.gzip_inhalt = str(dh.read(), "utf-8")

    def ausgabe(self):
        print(self.gzip_inhalt)

    def show_type(self):
        # zum testen den Typ von gzip_inhalt ausgeben, ob es wirklich ein string ist
        print(type(self.gzip_inhalt))


# def main():
#     In1 = MyGzip("py_ub5_aufgabe2.txt.gz")
#     In1.zip_read()
#     In1.ausgabe()
#     In1.show_type()


# if __name__ == "__main__":
#     main()
