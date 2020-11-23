import csv
from csv import writer
import sys
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def gunatiket(username,tiket) :
    clear_screen()
    print("|-----------------------------------------------|")
    print("|=======GUNAKAN TIKET WAHANA WILLY WANGKY=======|")
    print("|-----------------------------------------------|")
    print("\n")
    ID_Wahana = input('Masukkan ID wahana: ')
    Used_Date =  input('Masukkan tanggal hari ini: ')
    Used_Tiket = input('Jumlah tiket yang digunakan: ')
    list_penggunaan = [username, Used_Date, ID_Wahana, Used_Tiket]
    x = 0
    n = 0
    for row in tiket :
        n += 1
    for i in range(1,n):
        if (ID_Wahana == tiket[i][1]) and (username == tiket[i][0]) :
            if (int(Used_Tiket) <= int(tiket[i][2])):
            # menunjukkan nomor posisi id wahana yg akan di cek penggunaannya
                sisa_tiket = int(tiket[i][2]) - int(Used_Tiket)   
                pembaruan_tiket = sisaTiket(username,ID_Wahana,sisa_tiket,tiket)
                mydata = [True, pembaruan_tiket, list_penggunaan]
                break
            else:
                mydata = [False, []]
        else :
            mydata = [False, []]

    return mydata    
def sisaTiket(username,ID_Wahana,sisa_tiket,tiket):
    x = 0
    for row in tiket:
        x+=1
    for i in range(1,x):
        if username == tiket[i][0] and ID_Wahana == tiket[i][1]:
            tiket[i][2] = sisa_tiket
            return tiket
            break
