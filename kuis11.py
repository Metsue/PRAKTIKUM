'''
import math
def z (x):
    if x > 0:
        return math.sqrt(x)+x+1
    elif x<0:
        return x**3 - x + 1
    elif x == 0:
        return 0

x = int(input('masukkan nilai x ='))
print (f' jika x = {x} hasil dari z adalah = {z(x)}')'''


def kinetik (m,v):
    ek = (1/2)*m*v**2
    return ek

def momentum (m,v):
    p = m*v
    return p

print ('''
Pilih rumus :
1. Rumus energi kinetik
2. Rumus momentum''')

pilih = int(input('Pilih ='))
if pilih == 1 :
    m = int(input('masukkan nilai m ='))
    v = int(input('masukkan nilai v ='))
    ek = (1/2)*m*v**2
    print (f'hasil dari ek adalah = {ek}')
elif pilih == 2 :
    m = int(input('masukkan nilai m ='))
    v = int(input('masukkan nilai v ='))
    p = m*v
    print (f'hasil dari momentum adalah = {p}')
else:
    print ('harus pilih 1 atau 2')
    
    
