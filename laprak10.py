#Nomor 1 Indra
"""
def usd(rupiah):
    return rupiah * 0.000063
def eur(rupiah):
    return rupiah * 0.000060
def yen(rupiah):
    return rupiah * 0.0097

print ('''
Selamat datang di pilihan konversi mata uang
***======================================***
Silahkan mau mengkonversi rupiahnya ke mana?
1. Rupiah ke US Dolar (USD)
2. Rupiah ke Euro (EUR)
3. Rupiah ke Yen (JPY)
***======================================***
''')
ulang = 'y'
while ulang.lower() == 'y':
    pilih = int(input('Pilih mau mengkonversi ke (1/2/3) ='))
    if pilih == 1 :
        rupiah = int(input('Masukkan nominal rupiah yang ingin di konversi = Rp.'))
        print (f'Hasil konversi Rp.{rupiah} adalah = {usd(rupiah)} USD')
        ulang = input('Mau konversi ke mata uang lain? (y/n) =')
        print ('='*60)
    elif pilih == 2 :
        rupiah = int(input('Masukkan nominal rupiah yang ingin di konversi = Rp.'))
        print (f'Hasil konversi Rp.{rupiah} adalah = {eur(rupiah)} EUR')
        ulang = input('Mau konversi ke mata uang lain? (y/n) =')
        print ('='*60)
    elif pilih == 3 :
        rupiah = int(input('Masukkan nominal rupiah yang ingin di konversi = Rp.'))
        print (f'Hasil konversi Rp.{rupiah} adalah = {yen(rupiah)} Yen')
        ulang = input('Mau konversi ke mata uang lain? (y/n) =')
        print ('='*60)
    else:
        print('Maaf pilihan untuk konversi ke mata uang tersebut tidak ada!!')
        ulang = input ('Silahkan pilih sesuai list yang tertera lagi (y/n) =')
        print ('='*60)
"""


#Nomor 2 Indra
def f(x, a, b, c):
    nilai_fx = a * x**2 + b *x +c
    print('f(x) = ax**2 + bx + c')
    print(f'jika f({x}) = {a, x**2} + {b, x} + {c} maka jawabannya adalah = {nilai_fx}')
    return

#Nomor 3 Indra
'''
def gajih(jamker, gaji_perjam):
    if jamker > 40 :
        lemburan = (jamker - 40) * gaji_perjam * 1.5
        total =  (40 * gaji_perjam) + lemburan
    else:
        total = jamker * gaji_perjam
    return (total)

gaji_perjam = float(input('Masukkan gaji kamu perjam ='))
jamker = int(input('Masukkan jumlah jam kerja kamu dalam seminggu ='))
total = gajih(jamker, gaji_perjam)
print (f'Total gaji yang kamu peroleh adalah sebesar Rp.{total:,.2f}')'''



#Nomor 4 Indra
def harga_tiketmasuk(umur):
    if umur >= 0 and umur <=12:
        harga = 25000
    elif umur >= 13 and umur <= 21:
        harga = 40000
    elif umur >= 22 and umur <= 60:
        harga = 60000
    elif umur > 60:
        harga = 30000
    else:
        print ('Umur Tidak Diketahui')
    return (harga)

umur = int(input('Masukkan umur anda ='))
print (f'Harga tiket masuk bioskop yang harus kamu bayar = Rp.{harga_tiketmasuk(umur)} ')
            



















