zdefiniować funkcje z parametrami zwracające wyniki
def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def iloczyn(a, b):
    return * B

def iloraz(a, b):
    if b != 0:
        return a / b
    else:
        print('Błąd dzielenia przez zero!')

# dane wejściowe
a = float(input('Podaj liczbę: '))
b = float(input('Podaj liczbę: '))
operacja = input('Wybierz działanie (+, -, *, /): ')

# operacje
if operacja == '+':
    print(dodaj(a, b))
elif operacja == '-':
    pass

