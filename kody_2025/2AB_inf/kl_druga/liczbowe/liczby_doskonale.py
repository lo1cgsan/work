n = int(input('Podaj liczbę n: '))

def czy_doskonala(n):
    dzielniki = [1]
    suma_d = 1
    d = 2
    while d <= n / 2:
        if n % d == 0:
            dzielniki.append(d)
            suma_d += d
        d += 1

    if suma_d == n:
        print('Doskonała')
    else:
        print('Niedoskonała')
    return dzielniki

assert czy_doskonala(6) == [1, 2, 3]
