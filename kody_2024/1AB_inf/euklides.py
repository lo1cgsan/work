a = int(input('Podaj liczbę a: '))
b = int(input('Podaj liczbę b: '))

if a > 0 and b > 0:
    licznik = 0
    while a != b:
        licznik += 1
        print(a, b)
        if a > b:
            a -= b
        else:
            b -= a
    print(f'NWD = {a}. Powtórzeń: {licznik}.')
else:
    print('Błędne dane!')
