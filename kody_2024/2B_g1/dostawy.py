def sumuj_tv(n):
    suma_tv = 0
    for _ in range(n):
        a = int(input('Ile telewizorów? '))
        suma_tv += a
    return suma_tv

l_dostaw_tv = int(input('Ile dostaw? '))
print(sumuj_tv(l_dostaw_tv))
