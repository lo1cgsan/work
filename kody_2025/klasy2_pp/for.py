ile = int(input('Ile razy: '))

for i in range(ile):
    a = int(input('Podaj liczbę: '))
    b = int(input('Podaj liczbę: '))
    suma = a + b

    if b != 0:
        iloraz = a / b
    else:
        iloraz = "nie dziel przez zero"

    print(suma, iloraz)
