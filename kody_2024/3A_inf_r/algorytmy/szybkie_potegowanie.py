def dec2bin(liczba):
    """zamiana liczby dziesiętnej na binarną"""
    pass
    return l_bin


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
    k = bin(k)
    print(k[2:])
    pass

def main():
    x = float(input('Podaj podstawę: '))
    k = int(input('Podaj wykładnik: '))
    print('x^k = ', poteguj(x, k))


main()
