n = int(input('Podaj liczbę n: '))

def rozloz(n):
    i = 2
    wynik = []
    while i <= n:
        if n % i == 0:
            print(i, end=' ')
            wynik.append(i)
            n = n // i
        else:
            i += 1

    return wynik

assert rozloz(58) == [2, 2, 2, 7]
