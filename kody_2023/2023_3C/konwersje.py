def any2dec():



def main():
    pw = int(input('Podaj podstawę: '))
    lw = input('Podaj liczbę: ')

    l10 = any2dec(pw, lw)

    pd = int(input('Podaj podstawę docelową: '))
    lw = dec2any(pd, l10)


main()
