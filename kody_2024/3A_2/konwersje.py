def any2dec(l_wej, p=2):
    n = len(l_wej)
    l_dec = 0
    for cyfra in '753':
        print(int(cyfra) * p**(n-1))
        l_dec += int(cyfra) * p**(n-1)
        n -= 1
    return l_dec

def dec2any(l_dec, p):
    l_dec = int(l_dec)
    l_wyj = ''
    while l_dec > 0:
        reszta = l_dec % p
        l_wyj += str(reszta)
        l_dec //= p
    print(l_wyj)
    wypisz wspak l_wyj


def main():
    p = int(input('Podaj podstawę: '))
    l_wej = input('Liczba: ')
    l_wyj = dec2any(l_wej, p)
    print(l_wej, l_wyj)

print(dec2any(11, 2))
