import csv
from csv import writer
import sys
import os


def save_file(user,wahana,pembelian,penggunaan,tiket,refund,ks):
    with open(input('Masukkan nama File user: '), 'w', newline='') as write_obj:
        csv_writer = writer(write_obj)
        for row in user:
            csv_writer.writerow(row) #done
    with open(input('Masukkan nama File Daftar Wahana: '), 'w', newline='') as write_obj:
        csv_writer = writer(write_obj)
        for row in wahana:
            csv_writer.writerow(row) #done

    with open(input('Masukkan nama File Pembelian Tiket: '), 'w', newline='') as write_obj:
        csv_writer = writer(write_obj)
        for row in pembelian:
            csv_writer.writerow(row) #done
    with open(input('Masukkan nama File Penggunaan Tiket: '), 'w', newline='') as write_obj:
        csv_writer = writer(write_obj)
        for row in penggunaan:
            csv_writer.writerow(row) #done
    with open(input('Masukkan nama File Kepemilikan Tiket: '), 'w', newline='') as write_obj:
        csv_writer = writer(write_obj)
        for row in tiket:
            csv_writer.writerow(row)

    with open(input('Masukkan nama File Refund Tiket: '), 'w', newline='') as write_obj:
        csv_writer = writer(write_obj)
        for row in refund:
            csv_writer.writerow(row)

    with open(input('Masukkan nama File Kritik Saran: '), 'w', newline='') as write_obj:
        csv_writer = writer(write_obj)
        for row in ks:
            csv_writer.writerow(row)
    print('Data berhasil disimpan!')
    print("\n")
    input("Tekan Enter untuk mengakhiri program...")

