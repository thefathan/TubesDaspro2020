import csv
from csv import writer
import sys
import os
import B01
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def signup(user):
    clear_screen()
    print("|----------------------------------------------|")
    print("|=======SIGN UP PEMAIN BARU WILLY WANGKY=======|")
    print("|----------------------------------------------|")
    print("\n")
    x = 0
    status = False
    for row in (user):
        x += 1
    nama = input('Masukan nama pemain: ')
    ttl =  input('Masukan tanggal lahir pemain (DD/MM/YYYY): ')
    tbadan = input('Masukkan tinggi badan pemain (cm): ')
    while not(status):
        counter = 0
        uname = input('Masukkan username pemain: ')
        for i in range(x):
            if (uname == user[i][3]):
                print("username telah digunakan, silahkan masukkan username yang lain")
                break
            else:
                counter += 1
                uname = uname
        if (counter == x):
            status = True
    passw = input('Masukkan password pemain: ')
    list_of_elem = [nama, ttl, tbadan, uname, B01.encode(passw), "Pemain", 0]
    print("Pemain", nama, "berhasil ditambahkan")
    return list_of_elem
