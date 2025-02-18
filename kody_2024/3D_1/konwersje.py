def any2dec(l_wej, p):
    l_dec = 0
    n = len(l_wej)
    for cyfra in l_wej:
        wartosc = int(cyfra) * p**(n-1)
        n -= 1
        print(wartosc, "", end="")
        l_dec += wartosc

    return l_dec


def dec2any(l_dec, p):
    l_dec = int(l_dec)
    l_wyj = ''  # pusty ciąg znaków
    while l_dec > 0:
        reszta = l_dec % p
        l_wyj += str(reszta)
        l_dec //= p
    print(l_wyj)


def main():
    p = int(input('Podaj podstawę: '))
    l_wej = input('Podaj liczbę: ')
    # l_wyj = any2dec(l_wej, p)
    l_wyj = dec2any(l_wej, p)
    print()
    print(f"{l_wej}{p} = {l_wyj}(10)")

main()
