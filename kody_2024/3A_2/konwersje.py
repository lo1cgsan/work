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
    n = len(l_wyj)
    wspak = ''
    for i in range(len(l_wyj)):
        # wspak += l_wyj[n-1-i]
        wspak += l_wyj[-1-i]
    return wspak

def main():
    p = int(input('Podaj podstawę: '))
    l_wej = input('Liczba: ')
    l_wyj = dec2any(l_wej, p)
    print(l_wej, l_wyj)

main()
