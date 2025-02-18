def any2dec(l_wej, p):
    n = len(l_wej)  # liczba cyfr
    l_dec = 0
    for cyfra in l_wej:
        wartosc = int(cyfra) * p**(n-1)
        print(wartosc, "", end="")
        n -= 1
        l_dec += wartosc
    return l_dec


def wypisz_wstecz(tekst):
    for i in range(len(tekst)):
        print(tekst[i])


def dec2any(l_dec, p):
    l_dec = int(l_dec)
    l_wyj = ''  # pusty ciąg znaków
    while l_dec > 0:
        reszta = l_dec % p
        l_wyj += str(reszta)
        l_dec //= p

    l_wyj


def main():
    p = int(input('Podaj podstawę: '))
    l_wej = input('Podaj liczbę: ')
    l_wyj = dec2any(l_wej, p)
    print()
    print(f"{l_wej}({p}) = {l_wyj}(10)")

main()
