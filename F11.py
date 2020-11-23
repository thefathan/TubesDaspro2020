import csv
from csv import writer
import sys
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def isi_kritik(ks):
    clear_screen()
    print("|--------------------------------------------------|")
    print("|=======ISI KRITIK SARAN WAHANA WILLY WANGKY=======|")
    print("|--------------------------------------------------|")
    print("\n")
    import csv
    print("Kritik dan saran:")
    x = 0
    p = 0
    new_list = []
    for item in ks:
        x += 1
    for i in range(1,x):
        new_list += [ks[i]]
    for i in new_list:
        p+=1

    for i in range(p):
        new_list[i][0],new_list[i][2] = new_list[i][2],new_list[i][0]        

    for j in range(p-1,0,-1):
        for i in range(j):
            if new_list[i]>new_list[i+1]:
                penanda = new_list[i]
                new_list[i] = new_list[i+1]
                new_list[i+1] = penanda

    for i in range(p):
        new_list[i][0],new_list[i][2] = new_list[i][2],new_list[i][0]        

    for row in new_list:
        print(row[2], "|", row[1], "|", row[0], "|", row[3])