def any2dec(liczba, p=2):
    l_dec = 0  # początkowa wartość liczby dziesiętnej
    n = len(liczba)  # liczba znaków
    # odczytywanie kolejnych cyfr z liczba
    for cyfra in liczba:
        l_dec += int(cyfra) * p**(n-1)
        n -= 1  # zmniejsz wartość n o 1
    return l_dec


def dec2bin(l_dec, p=2):
    l_dec = int(l_dec)
    l_bin = ''
    while l_dec > 0:
        reszta = l_dec % p
        l_bin += str(reszta)
        l_dec //= p
    print(l_bin)


def main():
    # dane wejściowe
    p = int(input('Podaj podstawę: '))
    liczba = input('Podaj liczbę: ')
    # l_dec = any2dec(liczba, p)
    liczba_wyjsciowa = dec2bin(liczba, p)
    print(liczba, liczba_wyjsciowa)


main()  # wywołanie funkcji
