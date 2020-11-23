import csv
from csv import writer
import sys
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def kritiksaran(username):
    clear_screen()
    print("|--------------------------------------------------------------|")
    print("|=======TAMBAHKAN KRITIK SARAN UNTUK WAHANA WILLY WANGKY=======|")
    print("|--------------------------------------------------------------|")
    print("\n")
    id_wahana = input('Masukkan id wahana yang dikritik: ')
    tanggal_kritik =  input('Masukan tanggal kritik saran: ')
    isi_kritik = input('Masukkan isi kritikan dan saran: ')
    kolom_kritiksaran = [username, tanggal_kritik, id_wahana, isi_kritik]
    return kolom_kritiksaran