import gzip
import pickle


class MyGzip(object):

    def __init__(self, dateinname):
        self.dateiname = dateinname

    def zip_write(self):
        with open(self.dateiname, "rb") as f_in:
            with gzip.open(self.dateiname + ".gz", "wb") as f_out:
                f_out.writelines(f_in)

    def zip_read(self):
        # leist zuerst einen Byte-Strom im Binary Format ein
        with gzip.open(self.dateiname + ".gz", "rb") as gzfile:
            # mit der str() Funktion und "utf-8" Parameter, wird der Bytestrom in einen string konvertiert
            self.gzip_inhalt = str(gzfile.read(), "utf-8")

    def ausgabe(self):
        print(self.gzip_inhalt)

    def show_type(self):
        # zum testen den Typ von gzip_inhalt ausgeben, ob es wirklich ein string ist
        print(type(self.gzip_inhalt))