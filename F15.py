import csv
from csv import writer
import sys
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def jumlahtiketpemain(tiket,wahana):
    clear_screen()
    print("|----------------------------------------------|")
    print("|=======JUMLAH TIKET PEMAIN WILLY WANGKY=======|")
    print("|----------------------------------------------|")
    print("\n")
    searchUser = input('Masukkan username: ')
    # Asumsi username valid
    x = 0
    n = 0 
    print("Riwayat:")
    for row in tiket :
        x += 1
    for rows in wahana :
        n += 1
    for i in range (1,x):
        if(tiket[i][0] == searchUser):
            for j in range(1,n):
                if (tiket[i][1] == wahana[j][0]):
                    print(str(tiket[i][1]) + " | " + str(wahana[j][1]) + " | " + str(tiket[i][2]))
