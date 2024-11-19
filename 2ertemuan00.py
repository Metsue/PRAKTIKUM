def Lingkaran(r):
    return (22/7)*r*r

import math
def segitiga(s1,s2):
    sm= math.sqrt(s1**2 + s2**2)
    k = s1+s2+sm
    l = (1/2)*s1*s2
    return (sm,k,l)


def suhu(c):
    f = c*(9/5)+32
    k = c+ 273,15
    return (c,f,k)
c,f,k = suhu (90)
print (f'celcius = {c}, farrenhit = {f}, klvin = {k}')

def fungg
