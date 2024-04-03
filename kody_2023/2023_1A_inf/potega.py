def oblicz_potege(a, n):
    wynik = 1
    for i in range(n):
        wynik = wynik * a

    return wynik

def main():
    a = float(input('Podaj podstawę: '))
    n = int(input('Podaj wykładnik: '))
    print(oblicz_potege(a, n))


main()
