# konwersje.py
def any2dec(l_wej, p):
    n = len(l_wej)
    l_dec = 0

    for cyfra in l_wej:
        print(int(cyfra) * p**(n-1))
        l_dec += int(cyfra) * p**(n-1)
        n -= 1

    return l_dec

def dec2any(l_dec, p):
    l_wyj = ''

    while l_dec > 0:
        reszta = l_dec % p
        l_wyj += str(reszta)
        l_dec //= p
    print(l_wyj)

def main():
    l_wej = input('Podaj liczbę: ')
    p = int(input('Podaj podstawę: '))
    l_wyj = any2dec(l_wej, p)
    print(l_wej, l_wyj)

dec2any(11, 2)
