'''
import os
bil_1 = int(input('Masukkan bilangan 1 :'))
bil_2 = int(input('Masukkan bilangan 2 :'))

penj = bil_1 + bil_2
peng = bil_1 - bil_2
per  = bil_1 * bil_2
pemb = bil_1 / bil_2

print ('='*37)
print (f'| Hasil Penjumlahan |{bil_1} + {bil_2} = {penj}|')
print ('-'*37)
print (f'| Hasil Pengurangan |{bil_1} - {bil_2} = {peng}|')
print ('-'*37)
print (f'| Hasil Perkalian |{bil_1} * {bil_2} = {per}|')
print ('-'*37)
print (f'| Hasil Penjumlahan |{bil_1} / {bil_2} = {pemb}|')
print ('='*37)

os.system ('pause')
'''

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
a = int(input('Masukkan nilai ='))
if a >= 60  and a <=80 :
    print ('Anda lulus')
else:
    print ('Gambatte belajarnya >_<')'''

'''
n = int(input('Masukkan harga ='))
poin = int(input('Masukkan poin ='))
if n >=0 :
    if poin >= 150:
        dis = (n * 0.15)
        print (f'anda membayar ={n-dis}')
    else:
        disk = (n * 0.1)
        print (f'anda membayar ={n-disk}')
else:
    print ('Harus memasukkan harga lebih dari 0')'''

'''
n = 100
while n >= 0:
    print (n, end=' ')
    n -= 5'''


#UTS
'''
a = 1
b = 1
c = 2
d = 2
if a == b or c == d:
    print ('Benar')
else:
    print ('Salah')'''
'''
ulang = 0
while ulang <5:
    print ('Semangat UTS')
    ulang+=1'''

'''
for a in range (0, 5, 1):
    print ('Semangat UTS')'''
    
'''
Temp=0
for i in range(1, 4):
    for j in range(3, 5):
        if (i*j>=4)and (i*j<=10):
            Temp=Temp+i*j
            print (i*j, end =' ')
    print()
print(i,j, Temp)'''

'''
a = int(input('a ='))
if a <= 3:
    print (a+3)
    a=a-3
else:
    print(a)
if a>0:
    print (a)
    a=a*0
elif a<0:
    print(a*a)
else:
    a=0
print(a)'''

'''
t = int(input('Masukkan bilangan bulat ='))
for i in range (1, t+1):
    for k in range (t-i, 0, -1):
        print('',end=' ')
    for j in range (i, 0, -1):
        print('$', end=' ')
    print()'''


'''
n=int(input("masukkan angka ="))
for i in range(n):
    for j in range(n-i):
        print(, end = "\t" )
    print()'''




n = int(input("Masukkan angka = "))
for i in range(0, n+1,1):
    for j in range(n, 0,-1):
        if j > i:
            print(i*j, end="\t")
        print (end='')
    print()







