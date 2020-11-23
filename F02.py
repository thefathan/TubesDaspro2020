import csv
from csv import writer
import sys
import os
import B01

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def login(user):
    print("|--------------------------------|")
    print("|=======LOGIN WILLY WANGKY=======|")
    print("|--------------------------------|")
    print("\n")
    x = 0
    status = False
    for row in (user):
        x += 1
    while status == False:
        uname = input("Masukkan username: ")
        pw = input("Masukkan password: ")
        for i in range (1, x):
            if (uname == user[i][3]):
                if (B01.encode(pw) == user[i][4]):
                    dataUser = user[i]
                    status = True
                    break
                else:
                    status = False
            else:
                status = False

        if status == False:
            print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")

    if user[i][-2]=='Admin':
        print("Selamat datang Admin,", user[i][0] + "!")
        data = [uname, 'admin']
        return data
    elif user[i][-2]=='Pemain':
        print("Selamat bersenang-senang,", user[i][0] + "!")
        data = [uname, 'pemain']
        return data        