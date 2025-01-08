def czy_palindrom(tekst):
    ile = len(tekst)
    for i in range(ile//2):
        if tekst[i] != tekst[-1-i]:
            return False
    return True


def main():
    tekst = input('Podaj tekst: ').lower().replace(' ', '')
    if czy_palindrom(tekst):
        print('Palindrom.')
    else:
        print('Nie palindrom.')


main()
