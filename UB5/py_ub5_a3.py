from mygzip import MyGzip
# import gzip

# def erstelleGzipDatei():
#     f_in = open("namen.txt", "rb")
#     f_out = gzip.open("namen.txt.gz", "wb")
#     f_out.writelines(f_in)
#     f_out.close()
#     f_in.close()

def main():
    In1 = MyGzip("UB5/Files/namen.txt")
    In1.zip_write()
    In1.zip_read()
    In1.ausgabe()
    In1.show_type()


if __name__ == "__main__":
    main()
