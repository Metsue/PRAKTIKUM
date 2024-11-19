#NOMOR 1
# import os
print ('Game Gunting / Batu / Kertas')
print ('='*12,'***','='*11)

print ('Pilihan kamu =')
print ('# Gunting')
print ('# Batu')
print ('# kertas')
print ('-'*27)

saya = input('pilihan saya =')
bot = input('pilihan bot =')
print ('-'*27)

if saya.lower()== bot.lower():
    print ('seri')
else:
    if saya.lower()== 'gunting':
        if bot.lower() == 'kertas':
            print ('Saya menang')
        else: #jika bot (batu)
            print ('Bot menang')
    elif saya.lower() == 'batu':
        if bot.lower() == 'gunting':
            print ('Saya menang')
        else: #jika bot (kertas)
            print ('Bot menang')
    elif saya.lower() == 'kertas':
        if bot.lower() == 'batu':
            print ('Saya menang')
        else: #jika bot (gunting)
            print ('Bot menang')
#os.system ('pause')

#NOMOR 2
'''
print ('Menentukan tahun kabisat!!!')
print ('='*25)

tahun = int(input('Masukkan tahun ='))

if tahun % 400 == 0:
    print (f'{tahun} tersebut adalah tahun kabisat')
else:
    if tahun % 100 == 0:
        print (f'{tahun} tersebut bukan tahun kabisat')
    else:
        if tahun % 4 == 0:
            print (f'{tahun} adalah tahun kabisat')
        else:
            print (f'{tahun} tersebut bukan tahun kabisat')'''

#NOMOR 3
'''
a = int(input('Masukkan nilai a ='))
b = int(input('Masukkan nilai b ='))
op = input('Masukkan operasi matematika =')

if op == '+':
    hasil = a+b
    print (f'hasil perhitungan {a} + {b} adalah ={hasil}')
elif op == '-':
    hasil = a-b
    print (f'hasil perhitungan {a} - {b} adalah ={hasil}')
elif op == '*':
    hasil = a*b
    print (f'hasil perhitungan {a} * {b} adalah ={hasil}')
elif op == '<':
    if a < b:
        print (f'benar, bilangan {a} < bilangan {b}')
    else:
        print (f'salah')
elif op == '>':
    if a > b:
        print (f'benar, bilangan {a} > bilangan {b}')
    else:
        print (f'salah')
elif op == '=':
    if a == b:
        print ('benar')
    else:
        print ('salah')'''

#NOMOR 4
'''
nilai= int(input('Masukkan nilai ujian mahasiswa ='))
if nilai >= 50:
    if nilai >= 60:
        if nilai >= 70:
            if nilai >=80:
                if nilai >=85:
                    print ('nilai mahasiswa adalah A')
                else:
                    print ('nilai mahasiswa adlaah B+')
            else:
                print ('nilai mahasiswa adlaah B')
        else:
            print ('nilai mahasiswa adlaah C+')
    else:
        print ('nilai mahasiswa adlaah C')
else:
    print ('nilai mahasiswa adalah D')'''

#NOMOR 5
'''
print ('Survey kelayakan untuk mendapatkan kartu GYM!!')

umur =int(input('Masukkan umur ksmu ='))

if umur >= 18:
    kartu= input('Mendaftar kartu VIP / Reguler =')
    if kartu.lower() == 'reguler':
        print ('Kamu berhasil mendaftar dan mendapatkan kartu Reguler')
    else:
        if umur >= 25:
            print ('Kamu berhasil mendaftar dan mendapatkan kartu VIP')
        else:
            print ('Maaf kamu tidak memenuhi syarat untuk mendapatkan kartu VIP')
else:
    print ('Mohon maaf kamu tidak memenuhi syarat untuk memiliki kartu anggota GYM')
'''
