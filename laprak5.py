#Nomor 1 Indra
'''
for x in range (100, 0, -5):
    print (x, end = ' ' )'''

#Nomor 2
'''
a = 'indraGantenk'
b = 'bungas123'

while True:
    usr = input('Masukkan Username =')
    paswrd = input('Masukkan Password =')
    if usr == a and paswrd == b:
        print ('Selamat datang kembali tuan','\n')
        break
    else:
        print ('Username dan Password anda salah!!!','\n')'''

#Nomor 3 indra
a = int(input('Masukkan angka pertama ='))
b = int(input('Masukkan angka terakhir ='))
ganjil = 0
genap = 0

for i in range (a, b+1, 1):
    if i%2 == 0:
        genap+= 1
        print (f'{i} adalah bilangan (Genap)')
    else:
        ganjil+=1
        print (f'{i} adalah (Ganjil)')
        
print(f'jumlah angka yang ganjil adalah ={ganjil}')
print(f'jumlah angka yang genap adalah ={genap}')

#Nomor 4
'''
total = 0
for a in range(1, 11):
    print(a, end=' + ' if a < 10 else ' = ')
    total += a
print(total)'''



#Nomor 5 indra
'''
kata = input('Masukkan kata yang di inginkan: ')
jumlah = 0

for i in kata:
    if i.lower() == 'a':
        jumlah += 1

if jumlah > 0:
    print(f'Jumlah huruf a dari kata "{kata}" adalah = {jumlah}')
else:
    print(f'Tidak ada huruf a di dalam kata "{kata}"')'''









#BUATI
'''
b=int(input('nilai b='))
while b>0:
    print (b)
    b-=1


for a in range (b, 0, -1):
    print (a)'''

'''
print ('menghitung luas persegi panjang')
ulang = 'y'
while (ulang=='y' or ulang =='y'):
    l=int(input('lebar='))
    p=int(input('panjang='))
    print('luas= ',p,'x',l,'=',p*l)
    ulang=input('ulang?9ketik y jiks y =')'''

'''
a=0
for s in range (1, 4, 1):
    a=a+3*s
print (s,'\t',a)'''


'''
a=0
s=1
while s<4:
    a=a+3*s
    s+=1
print(s,'\t',a)'''

'''

t = int(input())
for i in range(1,t+1):
    for k in range(t-i,0,-1):
        print(' ',end=' ')
    for j in range(i,0,-1):
        print('$', end=' ')
    print()'''

'''
ulang = 'y'
while (ulang=='y' or ulang =='ya'):
c =0
for a in range (0, a):
    a = int(input('masukkan banyak data ='))
    c= sum+a
b= c/a
print (b)
ulang =input('ulang? ketik y atau ya =')'''

