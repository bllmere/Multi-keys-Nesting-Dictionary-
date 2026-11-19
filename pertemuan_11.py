# Program 11.1 Multi keys & Nesting Dictionary

import datetime

mahasiswa1 = {
    "nama"       : "cal faical",
    "nim"        : "19022001",
    "sks_lulus"  : 130,
    "beasiswa"   : "False",
    "lahir"      : datetime.datetime(2001,4,10)
}

mahasiswa2 = {
    "nama"       : "pras gupras",
    "nim"        : "19022002",
    "sks_lulus"  : 140,
    "beasiswa"   : "True",
    "lahir"      : datetime.datetime(2002,10,10)
}

mahasiswa3 = {
    "nama"       : "guh teguh",
    "nim"        : "19022003",
    "sks_lulus"  : 100,
    "beasiswa"   : "True",
    "lahir"      : datetime.datetime(1977,5,10)
}
data_mahasiswa = {
    "MAH001" : mahasiswa1,
    "MAH002" : mahasiswa2,
    "MAH003" : mahasiswa3,
}

print (f"{'KEY' :<6} {'Nama' :<6} {'SKS' :<6} {'Beasiswa' :<6} {'Lahir' :<6}") 
print ("-"*50)

for mahasiswa in data_mahasiswa :
    KEY = mahasiswa

    NAMA        = data_mahasiswa [KEY] ['nama']
    NIM         = data_mahasiswa [KEY] ['nim']
    SKS         = data_mahasiswa [KEY] ['sks_lulus']
    BEASISWA    = data_mahasiswa [KEY] ['beasiswa']
    LAHIR       = data_mahasiswa [KEY] ['lahir'].strftime("%x")

    print (f"{KEY :<6} {NAMA :<6} {SKS :<6} {BEASISWA :<6} {LAHIR :<6}") 

# Program 11.2 Laihan Dicrionary Bagian 1

import datetime

mahasiswa_template = {
    "nama"       : "nama",
    "nim"        : 0000000,
    "sks_lulus"  : 0,
    "lahir"      : datetime.datetime (1111,1,11)
}

data_mahasiswa = {}
print (f"{'SELAMAT DATANG': ^20}")
print (f"{'DATA MAHASISWA': ^20}")
print ("-"*20)

mahasiswa = dict.fromkeys (mahasiswa_template.keys())
print (mahasiswa)
mahasiswa ['nama']       = input ("Nama Mahasiswa")
mahasiswa ['nim']        = input ("Nim Mahasiswa")
mahasiswa ['sks_lulus']  = int(input ("SKS Lulus"))
TAHUN_LAHIR     = int(input("Tahun lahir (YYYY) : "))
BULAN_LAHIR     = int(input("Bulan lahir (1-12) : "))
TANGGAL_LAHIR   = int(input("Tanggal lahir (1-31) : "))
mahasiswa ['lahir'] = datetime.datetime (TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
print (mahasiswa)

# Program 11.3 Latihan Dictionary Bagian 2

import datetime
import os
import string
import random

# template dict mahasiswa

mahasiswa_template = {
    "nama"       : "nama",
    "nim"        : 0000000,
    "sks_lulus"  : 0,
    "lahir"      : datetime.datetime (1111,1,11)
}

data_mahasiswa = {}
while True :
    # os.system ("cls") # untuk windows
    os.system ("clear")
    print (f"{'SELAMAT DATANG' : ^20}")
    print (f"{'DATA MAHASISWA' : ^20}")
    print ("-"*20)
    mahasiswa = dict.fromkeys (mahasiswa_template.keys())
    print (mahasiswa)

    mahasiswa ['nama']       = input ("Nama Mahasiswa")
    mahasiswa ['nim']        = input ("Nim Mahasiswa")
    mahasiswa ['sks_lulus']  = int(input ("SKS Lulus"))
    TAHUN_LAHIR     = int(input("Tahun lahir (YYYY) : "))
    BULAN_LAHIR     = int(input("Bulan lahir (1-12) : "))
    TANGGAL_LAHIR   = int(input("Tanggal lahir (1-31) : "))
    mahasiswa ['lahir'] = datetime.datetime (TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in
range (6)))
    data_mahasiswa.update ({KEY : mahasiswa})

    # dari program sebelumnya, hilangkan beasiswa
    print (f"\n{'KEY' :<6} {'Nama' :<6} {'NIM' :<6} {'SKS Lulus' :<6}")
    {"'Tanggal Lahir' :<10"}
    print ('-'*60)

    for mahasiswa in data_mahasiswa :
        KEY = mahasiswa
        
        NAMA        = data_mahasiswa [KEY] ['nama']
        NIM         = data_mahasiswa [KEY] ['nim']
        SKS         = data_mahasiswa [KEY] ['sks_lulus']
        LAHIR       = data_mahasiswa [KEY] ['lahir'].strftime("%x")

        print (f"{KEY :<6} {NAMA :<6} {SKS :<6} {LAHIR :<6}")

    print ("\n")
    is_done = input("Mau tambah lagi bro (y/n)?")
    if is_done == "n" :
        break

print ("\n Akhiri program, terimakasih")