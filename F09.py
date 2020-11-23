import csv
from csv import writer
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def refundTiket(username,tiket,wahana,user):
    clear_screen()
    print("|---------------------------------------|")
    print("|=======REFUND TIKET WILLY WANGKY=======|")
    print("|---------------------------------------|")
    print("\n")
    ID_wahana = input("Masukkan ID wahana: ")
    tgl_refund = input("Masukkan Tanggal Refund: ")
    jml = input("Jumlah tiket yang di-refund: ")
    x = 0
    a = 0
    for row in tiket:
        x += 1
    for i in range (1, x):
        if (username == tiket[i][0]) and (ID_wahana == tiket[i][1]) and (int(jml) <= int(tiket[i][2])):
            hasil_refund = [username,tgl_refund, ID_wahana,jml]
            #mencari harga wahana dan harga tsb ditambahkan ke saldo
            perubahan_uang = hitungRefund(ID_wahana,jml,username,wahana,user)
            perubahan_tiket = dataTiket(ID_wahana,jml,username,tiket)
            mydata = [True, hasil_refund, perubahan_uang,perubahan_tiket]
            break
        else:
            mydata = [False, [], []]


    return mydata
#validasi apakah dia punya tiket atau tidak

def hitungRefund(ID_wahana,jml,username,wahana,user): #a adalah id wahana, jml adalah banyaknya tiket yang ingin direfund
    x = 0
    n = 0
    for row in wahana:
        x+= 1
    for row in user:
        n += 1
    for i in range(1,x):
        if ID_wahana == wahana[i][0]:
            potongan_harga = int(wahana[i][2])*0.2
            harga_refund = int(wahana[i][2]) - potongan_harga
            tambahan = harga_refund*int(jml)
            for j in range(1,n):
                if username == user[j][3]:
                    user[j][6] = int(user[j][6]) + int(tambahan)
                    break
    return user
    #perubahan yang terjadi di tiket

def dataTiket(ID_wahana,jml,username,tiket) :  
    p = 0
    for row in tiket:
        p+= 1
    for i in range(1,p):
        if username == tiket[i][0] and ID_wahana == tiket[i][1]:
            tiket[i][2] = int(tiket[i][2]) - int(jml)
            break
    return tiket
