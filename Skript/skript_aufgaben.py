# # x = 70
# # print(id(x)) # 140725194731456
# # print(hex(id(x))) # 0x7ffd233e2fc0

# # y = 11
# # print(id(y)) # 140725194729568
# # print(hex(id(y))) # 0x7ffd233e2860

# # z = x
# # print(id(z)) # 140725194731456
# # print(hex(id(z))) # 0x7ffd233e2fc0

# # x = 13
# # print(id(x)) # 140725194731456
# # print(hex(id(x))) # 0x7ffd233e2fc0

# # print(id(z)) # 140725194731456
# # print(hex(id(z))) # 0x7ffd233e2fc0

# # string = "Sven"
# # print(string)
# # string += " Birkenfeld AKFOE 50000 23123 123123 123123"
# # print(string)
# # # liste = string.split(" ", 1)
# # liste = string.partition("Birkenfeld")
# # print(liste)

# # dict_capitals = {"Deutschland": ["Berlin","Bonn"], "Niederland": "Amsterdam", "Frankreich": "Paris"}

# # dict_capitals2 = dict_capitals.copy()

# # print("vorher dict1:",dict_capitals)
# # print("vorher dict2:",dict_capitals2)

# # dict_capitals["Deutschland"] = ["Berlin","Bonn","Kreis Birkenfeld"]
# # print("nachher dict1:",dict_capitals)
# # print("nachher dict2:",dict_capitals2)

# # liste_woerter = ["a","a","b","c","a","d","x","y","x","b","i"]
# # set_woerter = set(liste_woerter)
# # print(set_woerter)
# # print(set_woerter.pop())
# # print(set_woerter)
# # print(set_woerter.pop())
# # print(set_woerter)
# # print(set_woerter.pop())
# # print(set_woerter)
# # print(set_woerter.pop())
# # print(set_woerter)

# # import time
# # from datetime import datetime
# # ts = time.time()
# # print(ts)
# # print(datetime.now())
# # print(datetime.utcfromtimestamp(ts))

# # temp1 = [36.5,37,37.5,39]
# # temp2 = []
# # F = map(lambda T: round(T*(9.0/5)+32,2),temp1)
# # print(list(F))

# # import functools
# # U = functools.reduce(lambda x,y: x+y, [47,11,42,13])
# # print(U)

# # import json

# # eintrag = {
# #     "Vorname": "Donald",
# #     "Nachname": "Duck",
# #     "Alter": 84
# # }

# # with open("eintrag.json", "w") as f:
# #     json.dump(eintrag,f)

# # s = json.dumps(eintrag)
# # print(s)

# # with open("eintrag.json", "r") as f:
# #     print(json.load(f))

# # a = json.loads(s)
# # for ele in a:
# #     print(ele)

# # import sys

# # def main():
# #     line = sys.argv

# # if __name__ == "__main__":
# # #     main()
# # import math

# # summe = 0

# # for i in range(10000000):
# #     zahl = ((-1)**i)/(2*i+1)
# #     summe += zahl

# # print("Zahl:", summe)
# # print("Pi/4:", math.pi/4)

# # def f(x=1,y=2,z=10):
# #     print(x,y,z)


# # f(1,2,3)
# # f(x=1,y=5,z=7)
# # f(y=1,z=3,x=5)
# # f()

# # import copy

# # l1 = [1,2,3]
# # print(l1)
# # l2 = [4,5,6]
# # l2 = copy.deepcopy(l1)

# # l1 = [1,2,3,4]
# # print(l1)
# # print(l1[-1])
# # print(l1[-1:])

# # tupel_queue = ("Sven","Thela","Philipp","Julian")
# # print(tupel_queue)
# # liste_queue = list(tupel_queue)
# # print(liste_queue)
# # liste_queue += ["Max"] # wie liste_queue.append("Max")
# # print(liste_queue)
# # tupel_queue = tuple(liste_queue)
# # print(tupel_queue)

# # s = "Hallo Welt!"
# # s = s + " Bye!"
# # print(s)
# # l2 = liste_queue.copy() # l2 = liste_queue[:]
# # print(l2)
# # liste_queue.append("Jan")
# # print(l2)
# # l2.append("Flo")
# # print(liste_queue)

# # s = "A"
# # print(s)
# # s2 = b'\xE2\x82\xAC'.decode("UTF-8")
# # s3 = b"A".decode("UTF-8")
# # s3 = bytes('A', "UTF-8")
# # s4 = b'\x41'.decode("UTF-8")
# # print(s4)

# # cities1 = set((("Python", "Perl"),("Paris", "Berlin", "London")))
# # print(cities1)
# # # cities2 = set((["Python", "Perl"],["Paris", "Berlin", "London"]))
# # # print(cities2)
# # cities3 = set([("Python", "Perl"),("Paris", "Berlin", "London")])
# # print(cities3)

# # A = 10

# # def eine_funktion(p1,p2,p3):
# #     global A
# #     print(A)
# #     A = 20
# #     print(A)
# #     # print(0 == False)

# # def main():
# #     eine_funktion(1,2,3)

# # if __name__ == "__main__":
# #     main()


# zeichenkette = "Diese Zahl ist ein Float mit zwei Nachkommastellen: {:.2f}".format(2.1111155)
# zeichenkette2 = "Diese Zahl ist ein Float mit zwei Nachkommastellen: %s" % 2.1111155
# print(type(zeichenkette))
# print(type(zeichenkette2))


# class AddClass(object):

#     def __init__(self, Faktor):
#         self.Proportional = Faktor

#     def __del__(self):
#         print("Destruktor: jetzt wird das Objekt abgebaut")
#         print("Dies ist aber nicht notwendig, da Python das selber handeln wuerde \n")

#     def print_ausgabe(self):
#         print("Dies ist eine einfache Ausgabe \n")

#     def daten_ausgabe(self):
#         print("Das Ergebnis lautet: " + str(self.CErgebnis) + " \n")

#     def kalkulation(self, a, b):
#         self.CErgebnis = self.Proportional * (a + b)

#         return(self.CErgebnis)

# def main():

#     myInstance = AddClass(10)

#     myInstance.print_ausgabe()

#     myInstance.daten_ausgabe()

#     Ergebnis = myInstance.kalkulation(1,2)


#     print(myInstance.__dict__)

#     print("\n")

#     del myInstance


# if __name__ == '__main__':
#     main()

# import numpy as np

# x = np.linspace(1,10, 10)
# print(x)
# a = np.array([1,2,3,4,5])
# print(a)
# b = a+a
# print(b)
# c = a*b
# print(c)
# print(type(c))

class Person(object):

    def __init__(self, vorname, nachname, geburtsdatum):
        self._vorname = vorname
        self._nachname = nachname
        self._geburtsdatum = geburtsdatum

    def setVorname(self, vorname):
        self._vorname = vorname

    def getVorname(self):
        return self._vorname

    def __str__(self):

        ret = self._vorname + " " + self._nachname
        ret += ", " + self._geburtsdatum
        return ret

    vorname = property(getVorname, setVorname)


class Angestellter(Person):

    def __init__(self, vorname, nachname, geburtsdatum, personalnummer):
        Person.__init__(self, vorname, nachname, geburtsdatum)
        # alternativ:
        #super().__init__(vorname, nachname, geburtsdatum)
        self.__personalnummer = personalnummer

    def __str__(self):
        # return super().__str__() + " " + self.__personalnummer
        # return Person.__str__(self) + " " + self.__personalnummer

        return super().vorname
        # return Person.getVorname(self)


if __name__ == "__main__":
    x = Angestellter("Homer", "Simpson", "09.08.1969", "007")
    print(x)


class Angestellter(Person):
def __init__(self, vorname, nachname, geburtsdatum, personalnummer):


Person.__init__(se1f, vorname, nachname, geburtsdatum)
# alternativ:
#super().__init__(vorname, nachname, geburtsdatum)
‘ self.__personalnummer = personalnummer


def __str__(self):


    # return super().__str__() + " " + selt.__personalnummer
    # return Person.__str__(self) + ” ” + self.__personalnummer
return super().vorname
# return Person.getVorname(se1f)
if __name__ == "__main__":
x = Angestellter("Homer", "Simpson", "09.08.1969", "007")
print(x)
