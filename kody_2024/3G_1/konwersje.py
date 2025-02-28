def any2dec(l_wej, p):
    n = len(l_wej)  # liczba znaków l_wej
    l_dec = 0
    for cyfra in l_wej:
        print(int(cyfra) * p**(n-1))
        l_dec += int(cyfra) * p**(n-1)
        n -= 1
    return l_dec


def dec2any(l_dec, p):
    l_dec = int(l_dec)
    l_wyj = ''  # pusty ciąg znaków
    while l_dec > 0:
        reszta = l_dec % p
        l_wyj += str(reszta)
        l_dec //= p
    n = len(l_wyj)
    wynik = ''
    for i in range(n):
        wynik += l_wyj[-1-i]
    return wynik

p = int(input('Podaj podstawę: '))
l_wej = input('Podaj liczbę: ')

l_wyj = dec2any(l_wej, p)

print(f"{l_wej}(10) =>  {l_wyj}({p})")
