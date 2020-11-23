import csv
from csv import writer
import sys
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def cariwahana(wahana):
    clear_screen()
    print("|-------------------------------------------|")
    print("|=======PENCARIAN WAHANA WILLY WANGKY=======|")
    print("|-------------------------------------------|")
    print("\n")
    status1 = False
    status2 = False
    print("Jenis batasan umur: \n1. Anak-anak (<17 tahun) \n2. Dewasa (>= 17 tahun)\n3. Semua umur \n\nJenis batasan tinggi badan: \n1. Lebih dari 170 cm\n2. Tanpa batasan")
    bup = input("Batasan umur pemain: ")
    while not(status1):
        if (bup == "1"):
            bup = "anak-anak"
            status1 = True
        elif (bup == "2"):
            bup = "dewasa"
            status1 = True
        elif (bup == "3"):
            bup = "semua umur"
            status1 = True
        else:
            bup = input("Pilihan tidak valid! \nmasukkan kembali angka pilihan anda(1/2/3): ")
    btb = input("Batasan tinggi badan: ")
    while not(status2):
        if (btb == "1"):
            btb = ">=170 cm"
            status2 = True
        elif (btb == "2"):
            btb = "tanpa batasan"
            status2 = True
        else:
            btb = input("Pilihan tidak valid! \nmasukkan kembali angka pilihan anda(1/2): ")
    x = 0
    counter = 0
    for row in (wahana):
        x += 1
    for i in range (x):
        if (wahana[i][3] == bup) and (wahana[i][4] == btb):
            print(wahana[i][0], "|", wahana[i][1], "|", wahana[i][2])
        else:
            counter += 1
    if (counter == x):
        print("Tidak ada wahana yang sesuai dengan pencarian kamu")
    else:
        print("")
