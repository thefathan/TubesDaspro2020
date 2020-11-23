import csv
from csv import writer
import sys
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def addwahana():
    clear_screen()
    print("|------------------------------------------------|")
    print("|=======TAMBAHKAN WAHANA BARU WILLY WANGKY=======|")
    print("|------------------------------------------------|")
    print("\n")
    #yang dapat mengisi adalah ketika defaul login admin
    print("Masukkan Informasi Wahana yang ditambahkan: ")
    id_wahana = input("Masukkan ID wahana baru: ")
    nama_wahana = input("Masukkan nama wahana baru: ")
    harga_tiket = input("Masukkan harga tiket: ")
    batasan_umur = input("Batasan umur (dewasa/anak-anak/semua umur): ")
    batasan_tinggi = input("Batasan tinggi badan (>=170 cm / tanpa batasan): ")
    kolom_wahana = [id_wahana, nama_wahana, harga_tiket, batasan_umur, batasan_tinggi]
    print("Wahana", nama_wahana, "berhasil ditambahkan!")
    return kolom_wahana