def fungsi1():
    print('selamat datang')
    print('mahasiswa baru')
    print('fkip ulm')

fungsi1()


def fungsi2(bil1, bil2, bil3):
    if bil2+bil3==0:
        print('ksalahan data')
        z=0
    else:
        z=(bil1+bil2)/(bil2+bil3)
    return(z)
'''
z= fungsi2(1,2,3)
print(z)
'''

'''
print(fungsi2(1,2,3))'''

x=int(input('x='))
y=int(input('y='))
t=int(input('t='))
z=fungsi2(x,y,t)
print(z)

def fungsi3(A, B):
    return(A+B-5)


print('fungsi3(', x, ',',y,')=',fungsi3(fungsi2(1,1,2),y))


def fungsi4(r):
    luas= 3,14 * (r**2)
    return luas

luas = fungsi4(r)
print(luas)


