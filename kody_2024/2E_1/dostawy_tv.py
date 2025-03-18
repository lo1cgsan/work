# dostawy_tv.py

def sumuj_tv(l_dostaw_tv):
    suma_tv = 0
    for _ in range(l_dostaw_tv):
        a = int(input('Ile tv? '))
        suma_tv = suma_tv + a
    return suma_tv

l_dostaw_tv = int(input('Ile dostaw? '))        
suma_tv = sumuj_tv(l_dostaw_tv)
print('Suma tv:', suma_tv)
