def czy_palindrom(tekst):
    ile = len(tekst)  # liczba znaków
    for i in range(ile // 2):
        if tekst[i] != tekst[-i-1]:
            return False
    return True


def main():
    tekst = input('Podaj tekst: ').strip().lower()
    if czy_palindrom(tekst):
        print('Palindrom.')
    else:
        print('Nie palindrom.')


main()
