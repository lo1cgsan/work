def nwd1(a, b):
    licznik = 0
    while a != b:
        licznik += 1
        print(a, b)
        if a > b:
            a -= b
        else:
            b -= a
    print(f'NWD = {a}. Powtórzeń: {licznik}.')

def nwd2(a, b):
    licznik = 0
    while b != 0:
        licznik += 1
        print(a, b)
        # k = b
        # b = a % b
        # a = k
        a, b = b, a % b

    print(f'NWD = {a}. Powtórzeń: {licznik}.')

a = int(input('Podaj liczbę a: '))
b = int(input('Podaj liczbę b: '))

if a > 0 and b > 0:
    # nwd1(a, b)
    nwd2(a, b)
else:
    print('Błędne dane!')
