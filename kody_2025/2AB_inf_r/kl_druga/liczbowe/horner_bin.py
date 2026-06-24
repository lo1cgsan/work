# Program oblicza wartość dziesiętną liczby binarnej
# za pomocą schematu Hornera

def oblicz_wielomian(wsp, x):
    wynik = wsp[0]
    for i in range(1, len(wsp)):
        wynik = wynik * x + wsp[i]
    return wynik

# dane wejściowe
alf = 'ABCDEF'
x = int(input('Podaj podstawę: '))
liczba = input('Podaj liczbę: ')
liczba = list(liczba)

for i in range(len(liczba)):
    cyfra = liczba[i]
    if cyfra.isdigit():
        liczba[i] = int(liczba[i])
    else:
        # zamiana litery na wartość całkowitą
        liczba[i] = ord(cyfra.upper()) - 55
        # liczba[i] = alf.index(cyfra.upper()) + 10

print(oblicz_wielomian(liczba, x))
