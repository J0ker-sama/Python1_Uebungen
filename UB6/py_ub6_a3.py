import os
import sys

def main():
    print("Aktuelles Verzeichnis:", end=" ")
    print(os.getcwd())

    print("Username: ", end=" ")
    print(os.getlogin())

    print("Festplattenauslastung: ", end=" ")
    print(os.cpu_count())

if __name__ == "__main__":
    main()