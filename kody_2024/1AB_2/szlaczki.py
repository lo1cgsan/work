# szlaczki.py

znak = input('Podaj znak: ')
n = int(input('Ile kolumn: '))
m = int(input('Ile wierszy: '))

for j in range(m):
    for i in range(n):
        print(znak, end='')
    print()
