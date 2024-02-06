import datetime
import os # buat clear/atasnya biar ngga kelihatan, terminal bawaan liblary python
import string
import random

template_data_mahasiswa = {
    'nama':'nama',
    'nim':'00000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}

Data_mahasiswa= {}

while True: # biar looping systemnya

    os.system('cls') # untuk windows
    # os.system('clear') # untuk mac

    print(f'{'SELAMAT DATANG':^20}') # kasih jarak dan agar tulisan ke tengah
    print(f'{'DATA MAHASISWA':^20}')
    print('='*20)

    mahasiswa = dict.fromkeys(template_data_mahasiswa.keys()) # menggunakan keys dari template

    mahasiswa['nama'] = input('Masukkan Nama : ')
    mahasiswa['nim'] = input('Masukkan Nim : ')
    mahasiswa['sks_lulus'] = int(input('Masukkan jumlah sks : '))
    TAHUN_LAHIR = int(input('Tahun lahir (yhyh): '))
    BULAN_LAHIR = int(input('Bulan lahir (1-12): '))
    TANGGAL_LAHIR = int(input('Tanggal lahir : '))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)


    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6))) # biar memilih random ada 6 kali
    Data_mahasiswa.update({KEY:mahasiswa}) # buat nambahin data ke data mahasiswa (ke distionary kosong)

    print(f'\n{'KEY':<8} {'Nama':<17} {'NIM':<8} {'SKS Lulus':<10} {'Tanggal Lahir':<16}')
    print('='*60)

    for mahasiswa in Data_mahasiswa:
        KEY = mahasiswa

        NAMA = Data_mahasiswa[KEY]['nama']
        NIM = Data_mahasiswa[KEY]['nim']
        SKS = Data_mahasiswa[KEY]['sks_lulus']
        LAHIR = Data_mahasiswa[KEY]['lahir'].strftime('%x') # biar tahun lahirnya seperti (1111/1/1)

        print(f'{KEY:<8} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^16}')

    print('\n')

    is_done = input('Tambah  Data mahasiswa Lagi ? (y/n) ') # buat tanya sudah apa belum agar system berhenti

    if is_done == 'n':
        break

print(f'{'\nEND PROGRAM, THANK YOU':^100}')