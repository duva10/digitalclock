#!/usr/bin/python
import sys
def utama():
    print "Maukah ente menjadi istriku ?"
    print "1 = Mau"
    print "2 = Tidak Mau"
    dipilih = raw_input("Pilih Nomor ( 1 / 2 ) : ")
    if dipilih == "1":
        print '"Aku berjanji akan cinta sampai mati sama kamu :* "'
    elif dipilih == "2":
        print '"Yahh jomblo lagi deh"'
    else :
        print "Pilihannya Cuma 1 Sama 2 Doang tong -_- "
    ulangi()
   
def ulangi():
    dicobalagi = raw_input("Coba lagi ? [Y/T] : ")
    if dicobalagi.lower() == "y":
        utama()
    elif dicobalagi.lower() == "t":
        sys.exit("Dadah :)")
    else :
        print "Pilihannya Cuma Y dan T Doang tong -_- "
        ulangi()

utama()