from math import sqrt
a = float(input('Podaj a: '))
b = float(input('Podaj b: '))
c = float(input('Podaj c: '))

delta = b**2 - 4 * a * c
if delta < 0:
    print('Brak pierwiastków')
elif delta == 0:
    x0 = -b / (2 * a)
    print(f'1 pierwiastek: {x0}')
else:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print(f'2 pierwiastki: {x1}, {x2}')
