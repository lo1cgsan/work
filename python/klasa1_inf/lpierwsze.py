def wypisz_pierwsze(n):
    for liczba in range(1, n + 1):
        pierwsza = True
        j = 2

        while j < liczba - 1:
            if liczba % j == 0:
                pierwsza = False
                break  # przerwij pętlę
            j += 1  # inkrementacja o 1
        
        if pierwsza:
            print(liczba)


def czy_pierwsza(liczba):
    j = 2
    while j < liczba - 1:
        if liczba % j == 0:
            pierwsza = False
            break  # przerwij pętlę
        j += 1  # inkrementacja o 1
    
    if pierwsza:
        print("Podan liczba jest pierwsza")
    else:
        print("Podan liczba nie jest pierwsza")


def main():
    """
    Program znajduje liczby pierwsze w zakresie <1; n>
    """
    # pobierz liczbę całkowitą i zapisz w zmiennej n
    n = int(input("Podaj n: "))
    # print(id(n))
    # wywołanie funkcji
    wypisz_pierwsze(n)
    
    n = int(input("Podaj n: "))
    czy_pierwsze(n)


main()
