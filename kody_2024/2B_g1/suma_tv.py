# suma_tv.py

def sumuj_tv(l_dostaw):
    dostawy = []  # utworzenie pustej listy
    suma_tv = 0
    for i in range(l_dostaw):
        a = int(input('Ile tv? '))
        dostawy.append(a)
        suma_tv = suma_tv + a

    print(dostawy)
    return suma_tv

l_dostaw_tv = int(input('Ile dostaw? '))
suma_tv = sumuj_tv(l_dostaw_tv)
print('Liczba tv:', suma_tv)
