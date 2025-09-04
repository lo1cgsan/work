def dec2bin(liczba, p):
    """zamiana liczby dziesiętnej na binarną"""
    reszty = []
    while liczba != 0:
        reszta = liczba % p
        if reszta > 9:
            pass
        reszty.append(reszta)
        liczba = liczba // p
    return reszty


def int_to_digit(value):
    # zamiana liczby na znak
    ASCII_0 = 48
    ASCII_A_10 = 55
    if 0 <= value <= 9:
        return chr(value + ASCII_0)
    elif 10 <= value <= 15:
        return chr(value + ASCII_A_10)
    else:
        return 0


def dec2any(value, base):
    if value == 0:
        return '0'
    wynik = ''
    while value > 0:
        wynik = int_to_digit(value % base) + wynik
        value = value // base
    return wynik


def poteguj(x, k):
    # k = dec2any(k, 2)
    # k = bin(k)
    # print(k[2:])
    # 6(10) = 110
    k = dec2bin(k, 2)
    k.reverse()
    p = x
    for i in range(1, len(k)):
        if k[i] == 1:
            p = p * p * x
        else:
            p = p * p
    print(p)

def main():
    x = float(input('Podaj podstawę: '))
    k = int(input('Podaj wykładnik: '))
    print('x^k = ', poteguj(x, k))


main()
