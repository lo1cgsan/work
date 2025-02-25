def any2dec(l_wej, p=2):
    n = len(l_wej)
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

    wypisz l_wyj wspak

def main():
    p = int(input('Podstawa: '))
    l_wej = input('Podaj liczbę: ')
    l_wyj = dec2any(l_wej, p)
    print(l_wej, l_wyj)

print(any2dec('1101', 2))
main()
