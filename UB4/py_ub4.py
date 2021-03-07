
def aufgabe1():
    zeichenkette = "[1,2,3,4, [a,b,c,d], help, run, [[a,b],[1,2]]]\n"
    print(zeichenkette)
    neu_liste = zeichenkette.split()

def main():
    aufgabe1()

if __name__ == "__main__":
    main()