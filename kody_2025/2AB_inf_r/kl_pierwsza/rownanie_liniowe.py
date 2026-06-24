# rownanie_liniowe.py
# a * x + b = 0
a = float(input('Podaj a: '))
b = float(input('Podaj b: '))

if a == 0:
    if b == 0:
        print('nieskończenie wiele rozwiązań')
    else:
        print('równanie sprzeczne')
else:
    x = -b / a
    print('x =', x)
