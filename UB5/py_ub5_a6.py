import json
import datetime
import time
from mydatenbank_a6 import MyDatenbank

# Uhrzeit und Datum: datetime.datetime.now()
# Unixzeit: time.time()

def jsonDateiErstellen():
    eintrag = {
        "datum": str(datetime.datetime.now()),
        "unix": int(time.time()),
        "primzahl": 7,
        "sensor": [-10,0,10]
    }

    with open("UB5/Files/eintrag.json","w") as jfile:
        json.dump(eintrag, jfile)

    s1 = json.dumps(eintrag) # macht ein String Object aus json Datein
    # dump in String = dump+s = dumps
    print("s1 =", s1) 
    # s1 = {"Datum und Uhrzeit": "2021-03-13 13:57:38.110830", "Unixzeitangabe": 1615640258, "Primzahl": 7, "S1": -10, "S2": 0, "S3": 10}
    print("type(s1) =",type(s1)) 
    # type(s1) = <class 'str'>

    objekt = json.loads(s1) # konviert einen String in Python Object
    print("objekt =", objekt)
    # objekt = {'Datum und Uhrzeit': '2021-03-13 13:57:38.110830', 'Unixzeitangabe': 1615640258, 'Primzahl': 7, 'S1': -10, 'S2': 0, 'S3': 10}
    print("type(objekt) =",type(objekt)) 
    # type(objekt) = <class 'dict'>

def jsonDateinAuslesen():
    with open("UB5/Files/eintrag.json","r") as jfile:
        s2 = json.load(jfile) # macht ein Python Object aus json Datein
    
    print("s2 =", s2)
    # s2 = {'Datum und Uhrzeit': '2021-03-13 13:57:38.110830', 'Unixzeitangabe': 1615640258, 'Primzahl': 7, 'S1': -10, 'S2': 0, 'S3': 10}

    print("type(s2) =",type(s2)) 
    # type(s2) = <class 'dict'>
    return s2


def main():
    jsonDateiErstellen()
    jsonDict = jsonDateinAuslesen()

    dbInst = MyDatenbank("UB5/Files/uebungsblatt5.db", "Aufgabe7")
    dbInst.connect()
    dbInst.generateTable()

    print("jsonDict:")
    for key in jsonDict:
        print(key)
    dbInst.schreibeInTabelle(jsonDict["datum"], jsonDict["unix"], jsonDict["primzahl"], jsonDict["sensor"])
    dbInst.leseVonTabelle()
        


if __name__ == "__main__":
    main()