'''
user = 'Aku adalah anak gembala'

perkecil1_huruf = user.lower()
perbesar_huruf = user.upper()

print (perkecil1_huruf, '\n',perbesar_huruf)'''

'''
user = input ('masukkan kata: ')
if user.lowe() == 'cerah':
    print ('matahari bersinar')'''

'''
bilangan_1 = int(input('masukkan bilangan 1 :'))
bilangan_2 = int(input('masukkan bilangan 2 :'))

if bilangan_1 < bilangan_2:
        if bilangan_1 > 0:
            print(bilangan_2/bilangan_1)
        else:
            print (f'bilangan{bilangan_1} tidak bisa di bagi dengan 0')
else:
    if bilangan_2 > 0:
        print(bilangan_1/bilangan_2)
    else:
        print(f'bilangan{bilangan_2} tidak bisa dibagi dengan 0')'''

'''
bilangan_1 = int(input('masukkan bilangan 1 :'))
bilangan_2 = int(input('masukkan bilangan 2 :'))

if bilangan_1 < bilangan_2 and bilangan_1 > 0:
    print (bilangan_2 / bilangan_1)

elif bilangan_1 > bilangan_2 and bilangan_2 > 0:
    print(bilangan_1 / bilsngsn_2)

else:
    print (f'bilangan tidak bisa di bagi dengan 0')'''

'''
print ('Arti dari kata bed')
indo = input('masukkan kata bahasa indo :')
if indo.lower() == 'kasur':
    print ('anda benarr yeyy')

else:
    print ('semngat belajar lagi b.inggris nya')'''

'''
print ('nilai mtk anda')
nil = int(input('masukkan nila Ai :'))
nil1 = int(input('masukkan nila B :'))

if nil >= 80 and nil1 >=80 :
    print ('Sangat Baik')


else:
    print ('anda belum lulus')'''


barang = input('apakah memiliki kartu : ya/tidak : ')
harga = int(input('masukkan harga :'))

if barang.lower() == 'ya':
    point = int(input('masukkan point :'))
    if point > 500:
        print (f' harga setelah diskon = {harga-harga*0.05}')
    else:
        print (f' harga setelah diskon = {harga-harga*0.02}')

else:
    print(f'anda tidak mendapat diskon dan membayar = {harga}')

          









