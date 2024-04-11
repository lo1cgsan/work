# Co to jest liczba pierwsza?
# Liczba która ma dwa dzielniki: 1 i samą siebie

def czy_pierwsza(liczba):
    for i in range(2, liczba-1):
        if liczba % i == 0:
            return False
    return True


a = int(input('Podaj liczbę: '))
if czy_pierwsza(a):
    print('Pierwsza')
else:
    print('Niepierwsza')
