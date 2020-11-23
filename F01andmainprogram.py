import csv
from csv import writer
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def show_menu1():
    print("\n")
    input("Tekan Enter untuk masuk/kembali ke menu...")
    clear_screen()
    print("           ___________________________________      ")
    print("          |                                   |     ")
    print("          |     MENU ADMIN WILLY WANGKY       |     ")
    print("          |___________________________________|     ")
    print('\n')
    print('\n')
    print("[1] SignUp User")
    print("[2] Search Pemain")
    print("[3] Lihat Kritik dan Saran")
    print("[4] Tambah Wahana")
    print("[5] Top Up Saldo Pemain")
    print("[6] Riwayat Penggunaan Wahana")
    print("[7] Jumlah Tiket Pemain")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")
    
    return selected_menu

def show_menu2():
    print("\n")
    input("Tekan Enter untuk masuk/kembali ke menu...")
    clear_screen()
    print("           ___________________________________      ")
    print("          |                                   |     ")
    print("          |     MENU PEMAIN WILLY WANGKY      |     ")
    print("          |___________________________________|     ")
    print('\n')
    print('\n')
    print("[1] Cari Wahana")
    print("[2] Beli Tiket")
    print("[3] Gunakan Tiket")
    print("[4] Ajukan Refund")
    print("[5] Berikan Kritik dan Saran")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")
    
    return selected_menu



# F02 - LOGIN
import F02
# F04-SIGN UP USER
import F04
# F05 - PENCARIAN PEMAIN
import F05
# F06 - PENCARIAN WAHANA
import F06
# F07 - PEMBELIAN TIKET
import F07
#F 08 - MENGGUNAKAN TIKET
import F08
#F09 - REFUNd
import F09
#F10 – KRITIK DAN SARAN 
import F10
#F11 - MELIHAT KRITIK DAN SARAN
import F11
#F12 - MENAMBAHKAN WAHANA BARU
import F12
# F13 - TOP UP SALDO
import F13
# F14 - MELIHAT RIWAYAT PENGGUNAAN
import F14
# F15 - MELIHAT JUMLAH TIKET PEMAIN
import F15
#  F16 - EXIT
import F16
# B01 - Enkripsi
#enkripsi ada di F02 alias login
# F16 - EXIT
import F16


######### PROGRAM UTAMA ################
# F01-LOAD FILE
user = []
with open(input("Masukkan nama File User: "), "r+") as file:
    a1 = csv.reader(file)
    for row in a1:
        user += [row]

wahana = []
with open(input("Masukkan nama File Daftar Wahana: "), "r+") as file:
    a1 = csv.reader(file)
    for row in a1:
        wahana += [row]

pembelian = []
with open(input("Masukkan nama File Pembelian Tiket: "), "r+") as file:
    a1 = csv.reader(file)
    for row in a1:
        pembelian += [row]
        
penggunaan = []
with open(input("Masukkan nama File Penggunaan Tiket: "), "r+") as file:
    a1 = csv.reader(file)
    for row in a1:
        penggunaan += [row]

tiket = []
with open(input("Masukkan nama File Kepemilikan Tiket: "), "r+") as file:
    a1 = csv.reader(file)
    for row in a1:
        tiket += [row]

refund = []
with open(input("Masukkan nama File Refund Tiket: "), "r+") as file:
    a1 = csv.reader(file)
    for row in a1:
        refund += [row]

ks = []
with open(input("Masukkan nama File Kritik dan Saran: "), "r+") as file:
    a1 = csv.reader(file)
    for row in a1:
        ks += [row]
    
    print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.")


# F03 - SAVE FILE

print(''' 
          __      __      __   ______     __        _______       __________       _____              _____      _______
          \ \    /  \    / /  |   ___|   |  |      /       |     /          \     |     \            /     |    |   ____|    
                                                      _____         ______                                          
           \ \  / /\ \  / /   |  |___    |  |     |  /          |  /      \  |    |   |\  \        /  /|   |    |   |___    
                                     |                                                                                  |
            \ \/ /  \ \/ /    |   ___|   |  |     |  |          | |        | |    |   |  \  \    /  /  |   |    |    ___|       
                                                                                                                     
             \  /    \  /     |  |___    |  |___  |  \_____     |  \______/  |    |   |    \  \/  /    |   |    |   |___
                                                                                                                    
              \/      \/      |______|   |______|  \_______|     \__________/     |___|      \__/      |___|    |_______|  


    ''')




log_in = F02.login(user)


if log_in[1] == 'admin':
    cek_keluar = False
    while cek_keluar == False:
        menu_admin = show_menu1()
        if(menu_admin == "1"): #sudah mantap
            sign_up = F04.signup(user)
            user += [sign_up]
            cek_keluar = False
        elif(menu_admin == "2"): #sudah mantap
            cari_pemain = F05.caripemain(user)
            cek_keluar = False
        elif(menu_admin == "3"): #wis mantap
            kritik = F11.isi_kritik(ks)
            cek_keluar = False
        elif(menu_admin == "4"): #sudah mantap
            tambah_wahana = F12.addwahana() #mantap
            wahana += [tambah_wahana]
            cek_keluar = False
        elif(menu_admin == "5"): #mantap
            top_up = F13.topup(user)
            user = top_up
            cek_keluar = False
        elif(menu_admin == "6"):
            F14.riwayat_wahana(penggunaan)
            cek_keluar = False
        elif(menu_admin == "7"):
            jmlh_tiket = F15.jumlahtiketpemain(tiket,wahana)
            cek_keluar = False
        elif(menu_admin== "0"):
            cek_keluar = True
            F16.keluar_program(user,wahana,pembelian,penggunaan,tiket,refund,ks)
        else: #diluar dari angka yang diberikan di menu 
            print("Kamu memilih menu yang salah!")
            cek_keluar = False


elif log_in[1] == 'pemain':
    cek_keluar = False
    while cek_keluar == False:
        menu_admin = show_menu2()
        if(menu_admin == "1"):
            F06.cariwahana(wahana) #mantap
            cek_keluar == False
        elif(menu_admin == "2"):
            buy_ticket = F07.belitiket(log_in[0],wahana,user) #
            if buy_ticket[2] == True:
                print('Selamat bersenang-senang di ', buy_ticket[3],'.')
                pembelian += [buy_ticket[0]]
                tiket += [buy_ticket[1]]
            elif buy_ticket[3] == False and buy_ticket[4] == True:
                print('Saldo Anda tidak cukup \nSilakan mengisi saldo Anda')
            elif buy_ticket[3] == True and buy_ticket[4] == False:
                print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini. \nSilakan menggunakan wahana lain yang tersedia.")
            cek_keluar == False
        elif(menu_admin == "3"):
            use_ticket = F08.gunatiket(log_in[0],tiket)
            if use_ticket[0] == True:
                tiket = use_ticket[1]
                penggunaan += [use_ticket[2]]
                print('Terima kasih telah bermain')
            elif use_ticket[0] == False:
                print("Tiket anda tidak valid dalam sistem kami")
            cek_keluar == False
        elif(menu_admin == "4"):
            ref_und = F09.refundTiket(log_in[0],tiket,wahana,user)
            if ref_und[0] == True:
                refund += [ref_und[1]]
                user = ref_und[2]
                tiket = ref_und[3]
                print("Uang refund sudah kami berikan pada akun Anda.")
            elif ref_und[0] == False:
                print("Anda tidak memiliki tiket terkait.")
            cek_keluar == False
        elif(menu_admin == "5"):
            comment = F10.kritiksaran(log_in[0])
            ks += [comment]
            cek_keluar == False
        elif(menu_admin == "0"):
            cek_keluar = True
            F16.keluar_program(user,wahana,pembelian,penggunaan,tiket,refund,ks)
        else:
            print("Kamu memilih menu yang salah!")
            cek_keluar == False

