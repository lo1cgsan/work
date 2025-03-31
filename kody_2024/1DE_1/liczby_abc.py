a = float(input('Podaj liczbę a: '))
b = float(input('Podaj liczbę b: '))
c = float(input('Podaj liczbę c: '))

if a > b:
    if a > c:
        print('a')
    else:
        print('c')
elif b > c:
    print('b')
else:
    print('c')

if a > b and a > c:
    print('a')
elif b > a and b > c:
    print('b')
else:
    print('c')
