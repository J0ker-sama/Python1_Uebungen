import importlib
import time
import py_rules_4connect


def istPrimezahl(zahl):
    istTeiler = False
    for i in range(2, zahl):
        if(zahl % i == 0):
            istTeiler = True
            break
    if(istTeiler == False):
        return True
    return False


def generischesProgrammieren():
    for i in range(2, 1000):
        # print("Local: " + str(i) + "\n")
        with open("py_rules_4connect.py", "a") as pyFile:
            neue_if_anweisung = "\n\n    if i == " + str(i) + ": " + "\n"
            pyFile.write(neue_if_anweisung)

            if(istPrimezahl(i)):
                neue_print_anweisung = "        return " + str(True) + "\n"
            else:
                neue_print_anweisung = "        return " + str(False) + "\n"
            
            pyFile.write(neue_print_anweisung)
        
        importlib.reload(py_rules_4connect)
        py_rules_4connect.print_output(i)
        
        #py_rules_4connect.print_output(i)

        # time.sleep(0.1)
    time.sleep(2)




def main():  
    generischesProgrammieren()


if __name__ == "__main__":
    main()

