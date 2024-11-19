#Nomor 1
'''
n = int(input('Masukkan nilai awal N ='))
m = int(input('Masukkan nilai akhir M ='))
for x in range (n, m+1, 1):
    if x % 2 == 0:
        print (f'{x} genap A')
    else:
        print (f'{x} ganjil B')'''


#Nomor 2
'''
x = 10
while x > 0:
    if (x<5 and x != 3):
        print (x)
    x = x-1'''

#Nomor 2
'''
for x in range (10, 0, -1):
    if (x < 5 and x != 3) :
        print (x)'''

#Nomor 3
'''
ulang = 'y'
while ulang == 'y':
    a = int(input('Masukkan bilangan pertama (A) ='))
    b = int(input('Masukkan bilangan kedua (B) ='))
    if a % b == 0:
         print (f'{a} adalah kelipatan dari bilangan {b}')
    else:
        print (f'{a} bukan kelipatan dari bilangan {b}')

    ulang = input('apakah anda ingin mengulang kembali? y/n =').lower()
    print('\n')
print ('terimakasih')'''

#Nomor 4
'''
n = int(input('masukkan nilai n ='))
genap =0
for i in range (1, n+1, 1):
    if i%2 == 0:
        genap+=1
print(f'Jumlah bilangan genap ada = {genap}')'''


#Nomor 5
'''
s = 0
x = 1
while x < 5:
    s = s+x
    x = x+3
print (x,s)'''

#Nomor 6
'''
ulang = 'ya'
while ulang == 'ya':
    a = int(input('Masukkan harga barang ='))
    n = int(input('masukkan berapa diskonnya ='))
    diskon = n/100
    potongan = a * diskon
    jmlh = a - potongan
    print (f'Harga sebelum diskon ={a}')
    print (f'Harga yang dipotong ={potongan}')
    print (f'Harga setelah diskon / Jumlah pembayaran ={jmlh}')
    ulang = input('Apakah anda ingin belanja lagi?? Ya/Tidak =').lower()
    print ('\n')
print ('terimakasih sudah berbelanja')'''



#Nomor 7
'''
data = int(input('Berapa banyak siswa yang didata ='))
a = 0
b = 0
while b < data:
    n= int(input(f'Tinggi siswa ke {b+1} ='))
    a+=n
    b+=1
if n > 0:
    c = a/data
    print (f'Rata-rata dari data tinggi badan siswa adalah = {c}')'''


#Nomor 8
print ("****== Selamat datang di toko ATK Indra Gantenk ==****")
print ("-"*50)
print ("Barang-barang yang tersedia di toko ATK saya yaitu :")

barang = {
'buku' : 5000,
'pulpen' : 3000,
'penghapus' : 2000,
'penggaris' : 4000,
'origami' : 6000,
'tipex' : 5000 }

for a, b in barang.items():
    print(f'{a} = {b}')
print ("="*27)

bayar = 0
while True:
    pilihan = input('Silahkan pilih barang =').lower()
    if pilihan in barang:
        bayar += barang[pilihan]
        print(f'Harganya = {bayar}')
    else:
        print ('Barang tidak ada.')
        continue
    tambah = input('\nIngin belanja lagi?? Y/n =').lower()
    if tambah == 'n':
        break
print ("="*27)
print(f'Jumlah harga pembayaran = Rp.{bayar}')

    

































    
