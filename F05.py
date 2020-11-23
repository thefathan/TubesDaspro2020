import csv
from csv import writer
import sys
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def caripemain(user):
    clear_screen()
    print("|-------------------------------------------|")
    print("|=======PENCARIAN PEMAIN WILLY WANGKY=======|")
    print("|-------------------------------------------|")
    print("\n")
    username = input("Masukkan username: ")
    x = 0
    temu = True
    for row in user:
        x += 1
    for i in range (1, x):
        if (username == user[i][3]):
            print("Nama Pemain:",user[i][0])
            print("Tinggi Pemain:",user[i][2])
            print("Tanggal Lahir Pemain:",user[i][1])
            temu = True
            break
        else:
            temu = False 
    if temu == False:
        print("Pemain tidak ditemukan")