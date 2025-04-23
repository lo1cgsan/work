"""
Program pobiera słowa w jęz. obcym i listę ich znaczeń
"""

def pobierz_znaczenia():
    znaczenia = input('Podaj znaczenie(a) oddzielone przecinkami:\n')
    znaczenia = znaczenia.split(',')
    znaczenia = [wyraz.strip() for wyraz in znaczenia]
    return znaczenia


def main():
    slownik = {}  # pusty słownik
    slowo = input('Podaj słowo: ').strip()

    while slowo:
        if slowo in slownik.keys():
            print('Słowo w bazie.')
            print(f"{slowo}: {','.join(slownik[slowo])}")
        else:
            slownik[slowo] = pobierz_znaczenia()

        slowo = input('Podaj słowo: ').strip()


main()
