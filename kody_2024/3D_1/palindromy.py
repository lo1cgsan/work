def czy_palindrom(tekst):
    for znak in tekst:
        print(znak)

    ile = len(tekst)
    for i in range(ile//2):
        if tekst[i] != tekst[-1-i]:
            return False
    return True


tekst = 'wakajak'
tekst[0] == tekst[4]
tekst[1] == tekst[3]

def main():
    tekst = input('Podaj tekst: ').lower()
    if czy_palindrom(tekst):
        print('Palindrom.')
    else:
        print('Nie palindrom.')


main()
