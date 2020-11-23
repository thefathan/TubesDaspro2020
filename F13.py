import csv
from csv import writer
import sys
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def topup(user):
    clear_screen()
    print("|----------------------------------------------|")
    print("|=======TOP UP SALDO PEMAIN WILLY WANGKY=======|")
    print("|----------------------------------------------|")
    print("\n")
    uname = input("Masukkan username: ")
    jmlah = int(input("Masukkan saldo yang di-top up: "))
    x = 0
    for row in user:
        x += 1
    for i in range (1,x):
        if (uname == user[i][3]):
            user[i][-1] = int(user[i][-1]) + jmlah
            print("Top up berhasil. Saldo", user[i][0], "bertambah menjadi", user[i][6])
            break
        else:
            i = i
    return user