import csv
from csv import writer
import sys
import os



def encode(kalimat):
    panjangpassword = 0
    abjad = ['3','c','b','d','o','f','i','9','g','j','l','k','8','z','e','p','2','r','0','t','w','v','u','x','y','n','h','1','m','5','q','4','a','6','s','7']
    for i in abjad:
        panjangpassword += 1
    kalimat = kalimat.lower()
    hasil_encode = ''
    for karakter in kalimat:
        if karakter in abjad:
          index_lama = abjad.index(karakter)
          index_baru = (index_lama + 3 ) % panjangpassword
          abjad_baru = abjad[index_baru]
          hasil_encode = hasil_encode + abjad_baru 
        else:
           hasil_encode = hasil_encode + '#' 
    return hasil_encode
