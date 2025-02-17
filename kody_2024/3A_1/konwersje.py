def bin2dec(l_bin, p=2):
    """
    params l_bin – liczba binarna
    params p – podstawa systemu liczbowego
    """
    n = len(l_bin)
    l_dec = 0
    for cyfra in l_bin:
        l_dec += int(cyfra) * p**(n-1)
        n -= 1
    return l_dec


def main():
    p = int(input('Podstawa: '))
    l_bin = input('Podaj liczbę: ')
    l_dec = bin2dec(l_bin, p)
    print(l_bin, l_dec)

main()
