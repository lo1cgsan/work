def wypisz_wielomian(stopien, wsp, x):
    for i in range(stopien):
        print(f'{wsp[i]}*{x}^{stopien-i}', end=' + ')
    print(wsp[-1])

def oblicz_wielomian(stopien, wsp, x):
    wynik = wsp[0]
    for i in range(1, stopien+1):
        wynik = wynik * x + wsp[i]
    return wynik

# dane wejściowe
stopien = 3
wsp = [2, 1, 4, 3]
x = 5

wypisz_wielomian(stopien, wsp, x)
wynik = oblicz_wielomian(stopien, wsp, x)
print(f'Wynik: {wynik}')
