def bin2dec(l_bin, p=2):
    """
    params l_bin – liczba binarna
    params p – podstawa systemu liczbowego
    """
    # 1011(2) = 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 1 * 2^0
    # len(), for, int()
    # do n przypisz długość l_bin
    n = len(l_bin)
    l_dec = 0
    for cyfra in l_bin:
        l_dec = l_dec + int(cyfra) * p**(n-1)
        n -= 1
    return l_dec

def dec2bin():
    pass

def main():
    p = int(input('Podaj podstawę: '))
    # 1. dane wejściowe: pobierz l_bin
    l_bin = input('Liczba binarana: ')
    # 2. do l_dec przypisz bin2dec(l_bin, 2)
    l_dec = bin2dec(l_bin, p)
    # 3. dane wyjściowe: wypisz l_bin i l_dec
    print(l_bin, l_dec)

main()
