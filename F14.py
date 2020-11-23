
import csv
from csv import writer
import sys
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def riwayat_wahana(penggunaan) :
    clear_screen()
    print("|----------------------------------------------------|")
    print("|=======RIWAYAT PENGGUNAAN WAHANA WILLY WANGKY=======|")
    print("|----------------------------------------------------|")
    print("\n")
    searchID = input('Masukkan ID Wahana: ')
    # Asumsi ID wahana valid
    x = 0
    print("Riwayat:")
    for row in penggunaan:
        x += 1
    for i in range (1,x):
        if( penggunaan[i][2] == searchID ) :
            print(str(penggunaan[i][1]) + " | " + str(penggunaan[i][0]) + " | " + str(penggunaan[i][3]))