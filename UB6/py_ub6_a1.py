import math
import numpy as np

def main():
    for i in np.arange(-1*(math.pi), (math.pi), 0.001):
        cosinus = math.cos(i)
        sinus = math.sin(i)
        tangens = math.tan(i)
        print("{}\t{}\t{}".format(sinus, cosinus, tangens))


if __name__ == "__main__":
    main()