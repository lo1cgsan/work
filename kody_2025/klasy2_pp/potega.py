# pobierz dane wejściowe
a = float(input('Podaj podstawę: '))
n = int(input('Podaj wykładnik: '))

wynik = 1
for i in range(n):
    print(f'{wynik} * {a}')
    wynik *= a

print(f'{a}^{n} = {wynik}')
