'''import math
a = math.pow (2,6)
b = math.ceil (4.6)
c = math.floor (4.6)
d = math.cos (90)
e = math.sin (90)
f = math.sqrt (9)

print (f"nilai dari a = {a} ")
print (f"nilai dari b = {b} ")
print (f"nilai dari c = {c} ")
print (f"nilai dari d = {d} ")
print (f"nilai dari e = {e} ")
print (f"nilai dari f = {f} ")'''

'''
import fractions
pecahan1 = fractions.Fraction(1,2)
pecahan2 = fractions.Fraction(2,4)
print (f"{pecahan1} + {pecahan2} = {pecahan1} + {pecahan2}")

from fractions import Fraction
pecahan1 = Fraction (1,2)
pecahan2 = Fraction (2,4)
print (f"{pecahan1} + {pecahan2} = {pecahan1} + {pecahan2}")'''

'''
cuaca = input("cuaca hari ini : ")
if cuaca == "cerah":
    print("matahari bersinar")'''

'''
total_belanja= int(input("total harga belanja ="))
if (total_belanja >= 100000):
    diskon = total_belanja*10/100
    total_bayar = total_belanja - diskon
    print (f"dengan total belanja Rp. {total_belanja} mendapat diskon sebanyak 10%, jadi harga yang harus dibayar Rp. {total_bayar}")'''

'''
nilai_uts = int(input("nilai uts ="))
if nilai_uts > 70 :
    print("Pertahankan nilainya dan semangat")
else:
    print("Jangan menyerah dan belajar lagi")

jawaban = 5*25
nilai = 0
jwbn = int(input("berapakah hasil dari 5 x 25  = "))

if jawaban == jwbn :
    nilai += 10
    print(f"Jawaban benar, nilai anda adalah {nilai}")
else:
    print ("jawaban salah, nilai anda adalah (0)")'''

'''
bilangan = int(input("masukan sebuah bilangan ="))
if bilangan > 0:
    print(f"{bilangan} adalah bilangan positif.")
elif bilangan < 0:
    print(f"{bilangan} ini adalah bilangan negatif.")
else:
    print(f"{bilangan} ini adalah 0")'''

a = int (input("masukkan bilangan ="))
if a % 2 == 0 :
    print ("bilangan tersebut genap")

else:
    print ("bilangan ganjil")
