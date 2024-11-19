'''import math
print ("Menentukan hasil dari akar 2 pangkat 4\n")
nilai = math.pow(2,4)
a= math.sqrt(nilai)

print (f" Hasil dari \u221A2\u2074 adalah = {a}")'''
'''
print ("Membuat program untuk menghitung penjumlahan, pengurangan,dan perkalian dari 2 bilangan pecahan!!")
from fractions import Fraction
pec1 = int(input("Masukkan nilai pembilang pecahan pertama ="))
pem1 = int(input("Masukkan nilai penyebut pecahan pertama ="))
pec2 = int(input("Masukkan nilai pembilang pecahan kedua ="))
pem2 = int(input("Masukkan nilai penyebut pecahan kedua ="))

frac1= Fraction(pec1, pem1)
frac2= Fraction(pec2, pem2)

#RUMUS PENJUMLAHAN, PENGURANGAN, DAN PERKALIAN
penj = frac1 + frac2
kur = frac1 - frac2
kali = frac1 * frac2

print("-"*45)
print(f"Hasil penjumlahan dari bilangan pecahan tersebut = {penj}")
print(f"Hasil pengurangan dari bilangan pecahan tersebut = {kur}")
print(f"Hasil perkalian dari bilangan pecahan tersebut = {kali}")'''

'''
import math
print ("Menghitung sebuah volume dari inputan nilai jari-jari(r)!!")
print ("-"*35)
r = int(input("Masukkan nilai jari-jari (r) ="))
v= (4/3)* math.pi * (r**3)
#hasil dari perhitungan tersebut..
print (f"Hasil dari nilai volume(V)tersebut adalah = {v}")'''

'''
print("Menentukan angka terbesar dari 3 nilai inputan!!!")
a = int(input("Masukkan angka pertama ="))
b = int(input("Masukkan angka kedua ="))
c = int(input("Masukkan angka ketiga ="))

maks = max(a,b,c)
print (f"Jadi angka terbesar dari ketiga bilangan tersebut adalah ={maks}")'''

print ("****== Selamat datang di toko ATK Indra ==****")
print ("-"*50)
print ("Barang-barang yang tersedia di toko ATK saya yaitu :")


buku = 5000
pulpen = 3000
penghapus = 2000
penggaris = 4000
origami = 6000
tipex = 5000

print (f"Harga buku = Rp.{buku}")
print (f"Harga pulpen = Rp.{pulpen}")
print (f"Harga penghapus = Rp.{penghapus}")
print (f"Harga penggaris = Rp.{penggaris}")
print (f"Harga origami = Rp.{origami}")
print (f"Harga tipe-x = Rp.{tipex}")
beli = input("Mau membeli barang  =")
print ("="*27)

if beli == "buku":
    print (f"Anda membayar = Rp.{buku}")
elif beli == "pulpen":
    print (f"Anda membayar = Rp.{pulpen}")
elif beli== "penghapus":
    print (f"Anda membayar = Rp.{penghapus}")
elif beli == "penggaris":
    print (f"Anda membayar = Rp.{penggaris}")
elif beli == "origami":
    print (f"Anda membayar = Rp.{origami}")
elif beli == "tipex":
    print (f"Anda membayar = Rp.{tipex}")
else:
    print ("Barang tersebut tidak ada")



