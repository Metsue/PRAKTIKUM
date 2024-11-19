#Nomor 1 indra
'''
import os
bil_1 = int(input('Masukkan bilangan 1 :'))
bil_2 = int(input('Masukkan bilangan 2 :'))

penj = bil_1 + bil_2
peng = bil_1 - bil_2
per  = bil_1 * bil_2
pemb = bil_1 / bil_2

print ('='*32)
print (f'Hasil Penjumlahan |{bil_1} + {bil_2} = {penj}|')
print ('-'*32)
print (f'Hasil Pengurangan |{bil_1} - {bil_2} = {peng}|')
print ('-'*32)
print (f'Hasil Perkalian |{bil_1} * {bil_2}   = {per}|')
print ('-'*32)
print (f'Hasil Pembagian |{bil_1} / {bil_2} = {pemb}|')
print ('='*32)

os.system ('pause')'''

#Nomor 2 indra
'''
import fractions
a = int(input('Masukkan pembilang pertama ='))
b = int(input('Masukkan penyebut pertama ='))
c = int(input('Masukkan pembilang kedua ='))
d = int(input('Masukkan penyebut kedua ='))

frac1 = fractions.Fraction(a, b)
frac2 = fractions.Fraction(c, d)

penj = frac1 + frac2

print (f'Hasil dari penjumlahan pecahan tersebut adalah ={penj}')'''


'''
#Nomor 3 indra
a = int(input('Masukkan nilai UTS ='))
b = int(input('Masukkan nilai UAS ='))
c = int(input('Masukkan nilai TUGAS ='))
if a and b >= 70  and c >=80 :
    print ('Anda lulus')
else:
    print ('Makanya menggawi laprak jangan pakai chat GPT')'''


#Nomor 4 indra
'''
import math
n = int(input('Masukkan harga ='))
a = input('Apakah anda memiliki voucher belanja?? Ya/Tidak =')
if a.lower() == 'ya':
    poin = int(input('Masukkan poin voucher ='))
    if n >=0 :
        if poin >= 100:
            x = int(input('Masukkan tahun lahir ='))
            tahun =math.floor(x / poin) / 100
            dis = tahun * n
            print (f'anda membayar dengan total harga =Rp.{n-dis:.0f}')
        else:
            disk = (n * 0.1)
            print (f'anda membayar dengan total harga =Rp.{n-disk:.0f}')
    else:
        print ('Harus memasukkan harga lebih dari 0')
else:
    print (f'anda membayar dengan total harga =Rp.{n}')'''

#Nomor 5 indra
'''
x = 0
y = 0
while x >= -4 and y <= 4:
    print (y, x, end=' ')
    x -= 1
    y += 1'''

#Nomor 6 indra
'''
a = 'indraBungas'
b = 'bungasbanar123'
ulang = 0
maks = 3

while ulang < maks:
    usr = input('Masukkan Username: ')
    paswrd = input('Masukkan Password: ')
    
    if usr == a and paswrd == b:
        print('Selamat datang kembali tuan!\n')
        break
    else:
        ulang += 1
        print('Username atau Password anda salah!!!')
        if ulang < maks:
            print(f'Anda telah mencoba {ulang} kali. Silakan coba lagi.')
        else:
            print('Hacker Jangan Mencuri >_<!')'''

#Nomor 7 indra
'''
for k in range (2, 6+1, 1):
    print (k**2)'''

#Nomor 8 indra
for a in range (1, 10+1, 1):
    print (f'{a} = {a*a+a}')

















