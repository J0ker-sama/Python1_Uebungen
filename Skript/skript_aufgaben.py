# x = 70
# print(id(x)) # 140725194731456
# print(hex(id(x))) # 0x7ffd233e2fc0

# y = 11
# print(id(y)) # 140725194729568
# print(hex(id(y))) # 0x7ffd233e2860

# z = x
# print(id(z)) # 140725194731456
# print(hex(id(z))) # 0x7ffd233e2fc0

# x = 13
# print(id(x)) # 140725194731456
# print(hex(id(x))) # 0x7ffd233e2fc0

# print(id(z)) # 140725194731456
# print(hex(id(z))) # 0x7ffd233e2fc0

# string = "Sven"
# print(string)
# string += " Birkenfeld AKFOE 50000 23123 123123 123123"
# print(string)
# # liste = string.split(" ", 1)
# liste = string.partition("Birkenfeld")
# print(liste)

# dict_capitals = {"Deutschland": ["Berlin","Bonn"], "Niederland": "Amsterdam", "Frankreich": "Paris"}

# dict_capitals2 = dict_capitals.copy()

# print("vorher dict1:",dict_capitals)
# print("vorher dict2:",dict_capitals2)

# dict_capitals["Deutschland"] = ["Berlin","Bonn","Kreis Birkenfeld"]
# print("nachher dict1:",dict_capitals)
# print("nachher dict2:",dict_capitals2)

# liste_woerter = ["a","a","b","c","a","d","x","y","x","b","i"]
# set_woerter = set(liste_woerter)
# print(set_woerter)
# print(set_woerter.pop())
# print(set_woerter)
# print(set_woerter.pop())
# print(set_woerter)
# print(set_woerter.pop())
# print(set_woerter)
# print(set_woerter.pop())
# print(set_woerter)

# import time
# from datetime import datetime
# ts = time.time()
# print(ts)
# print(datetime.now())
# print(datetime.utcfromtimestamp(ts))

# temp1 = [36.5,37,37.5,39]
# temp2 = []
# F = map(lambda T: round(T*(9.0/5)+32,2),temp1)
# print(list(F))

# import functools
# U = functools.reduce(lambda x,y: x+y, [47,11,42,13])
# print(U)

# import json

# eintrag = {
#     "Vorname": "Donald",
#     "Nachname": "Duck",
#     "Alter": 84
# }

# with open("eintrag.json", "w") as f:
#     json.dump(eintrag,f)

# s = json.dumps(eintrag)
# print(s)

# with open("eintrag.json", "r") as f:
#     print(json.load(f))

# a = json.loads(s)
# for ele in a:
#     print(ele)

# import sys

# def main():
#     line = sys.argv

# if __name__ == "__main__":
#     main()
import math

summe = 0

for i in range(10000000):
    zahl = ((-1)**i)/(2*i+1)
    summe += zahl

print("Zahl:", summe)
print("Pi/4:", math.pi/4)