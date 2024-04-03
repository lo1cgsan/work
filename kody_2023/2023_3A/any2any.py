def any2dec(l, p):
    wynik = 0

    d = len(l)
    for i in range(d - 1, -1, -1):
        wynik += int(l[i]) * p**(len(l) - i - 1)

    print(wynik)

def main():
    pw = int(input('Podaj podstawę: '))
    liczba = input('Podaj liczbę: ')
    any2dec(liczba, pw)


main()
