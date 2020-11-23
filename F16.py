import csv
from csv import writer
import sys
import os
import F03

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def keluar_program(user,wahana,pembelian,penggunaan,tiket,refund,ks):
    clear_screen()
    print("-EXIT-")
    z = input('Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ')
    if z == 'Y' or z == 'y':
        F03.save_file(user,wahana,pembelian,penggunaan,tiket,refund,ks)
    elif z == 'N' or z=='n':
        sys.exit()
