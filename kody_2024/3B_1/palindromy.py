def czy_palindrom(wyraz):
    liczba_znakow = 0
    for znak in wyraz:
        liczba_znakow += 1

    print(liczba_znakow)

    liczba_porownan = liczba_znakow // 2

    print(liczba_porownan)

    for i in range(liczba_porownan):
        print(wyraz[i], wyraz[liczba_znakow - 1])
        if wyraz[i] != wyraz[liczba_znakow - 1 - i]:
            return False

    return True

def main():
    wyraz = input('Podaj wyraz: ')
    if czy_palindrom(wyraz):
        print('Palindrom.')
    else:
        print('Nie palindrom.')


main()
