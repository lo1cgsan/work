# napisz program, który wypisuje n znaków
# w 1 wierszu

def wypisz_znak(z, n):
    for _ in range(n):
        print(z, end='')


znak = input('Podaj znak: ')
l_znakow = int(input('Podaj liczbę: '))

wypisz_znak(znak, l_znakow)
print()
wypisz_znak('@#', 20)
