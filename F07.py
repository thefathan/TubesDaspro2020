# Proses pembelian tiket

import csv
from csv import writer
import sys
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def isUmurValid(tlahir,tbeli,no,wahana):
    # hitung umur
    bulan_lahir = int(tlahir[1])
    bulan_beli = int(tbeli[1])
    tahun_lahir = int(tlahir[2]) 
    tahun_beli = int(tbeli[2])
    hari_lahir = int(tlahir[0])
    hari_beli = int(tbeli[0])

    if (bulan_lahir) > (bulan_beli): #artinya sudah ulangtahun
        umur = tahun_beli - tahun_lahir
    elif (bulan_lahir) < (bulan_beli): #artinya dia belum ulang tahun
        umur = tahun_beli - tahun_lahir - 1
    else: #kondisi dimana bulan kelahiran sama dengan bulan pembelian tiket
        if (hari_lahir) < (hari_beli): #artinya dia belum ulang tahun
            umur = tahun_beli - tahun_lahir - 1
        else: #kondisi dimana hari ulangtahun dia sudah dilewati atau hari itu dia ulang tahun
            umur = tahun_beli - tahun_lahir    
    # cek sesuai batas umur wahana

    if wahana[no][3]=='semua umur':
        data = [True, umur]
        return data

    elif umur >= 17:
        if wahana[no][3] == 'dewasa' or wahana[no][3] =='semua umur' :
            data = [True, umur]
            return data
        elif wahana[no][3] == 'anak-anak':
            data = [False, umur]
            return data

    elif umur < 17 : 
        if wahana[no][3] == 'semua umur' or wahana[no][3] == 'anak-anak' :
            data = [True, umur]
            return data
        elif wahana[no][3] == 'dewasa':
            data = [False, umur]
            return data

def isTinggiValid(i,no,wahana,user):
    # kategori tinggi
    if int(user[i][2]) >= 170:
        if wahana[no][4] =='tanpa batasan' or wahana[2][4] == '>=170 cm':
            data = [True,user[i][2]]
            return data
    elif int(user[i][2]) < 170:
        if wahana[no][4] == '>170 cm':
            data = [False,user[i][2]]
            return data
        elif wahana[no][4] =='tanpa batasan':
            data = [True,user[i][2]]
            return data

def isSaldoCukup(i,j,x,wahana,user):
    price = (int(wahana[j][2]))*int(x) 
    money = int(user[i][6])
    if money >= price :
        sisa_uang = money - price
        user[i][6] = sisa_uang
        return True
    else:
        return False
    
def belitiket(username,wahana,user):
    clear_screen()
    print("|-------------------------------------------------|")
    print("|=======PEMBELIAN TIKET WAHANA WILLY WANGKY=======|")
    print("|-------------------------------------------------|")
    print("\n")
    ID_Wahana = input('Masukan ID wahana: ')
    Tanggal_Pembelian =  input('Masukan tanggal hari ini: ')
    Jumlah_Tiket = input('Jumlah tiket yang dibeli: ')
    x = 0
    n = 0
    for row in wahana :
        n += 1
    for j in range(1,n):
        if (ID_Wahana == wahana[j][0]):
            no = j  # menunjukkan nomor posisi id wahana yg sesuai
    for row in user :
        x += 1
    for i in range(1,x):
        if (username == user[i][3]):
            tlahir = (user[i][1]).split('/')
            tbeli = (Tanggal_Pembelian).split('/')
            
            isSaldoValid = isSaldoCukup(i,no,Jumlah_Tiket,wahana,user)
            
            cukupUmur = isUmurValid(tlahir,tbeli,no,wahana)
            
            cukupTinggi = isTinggiValid(i,no,wahana,user)


            if (cukupUmur[0] == False) or (cukupTinggi[0] == False) : #kondisi dia tidak memenuhi persyaratan tinggi ataupun umur
                
                mylist = [[],[],[],True,False]
                
                return mylist

            elif (isSaldoValid == False) and (cukupUmur[0] == True) and (cukupTinggi[0] == True) :
                
                mylist = [[],[],[],False,True]
                
                return mylist
            elif isSaldoValid == True and (cukupUmur[0] == True) and (cukupTinggi[0] == True): # pemain memenuhi syarat wahana
                
                hasilpembelian = [username, Tanggal_Pembelian, ID_Wahana, Jumlah_Tiket]
                
                hasiltiket = [username, ID_Wahana, Jumlah_Tiket]
                
                mylist = [hasilpembelian,hasiltiket,True,wahana[no][1]]
                
                return mylist

