from math import pi, cos, radians

def cosinus1():
    stopien = 0.0
    radian = stopien * pi / 180
    licznik = 1
    while cos(radian) > 0:
        print('Licznik:', licznik)
        print(f'cos({stopien}) = {cos(radian)}')
        stopien += 10.0
        radian = stopien * pi / 180
        licznik += 1

def cosinus2():
    for stopien in range(0, 100, 10):
        wynik = cos(radians(stopien))
        print(f'cos({stopien}) = {round(wynik, 2)}')


cosinus2()
