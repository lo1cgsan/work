# funkcje.py

def szlaczek(znak, n):
    for _ in range(n):
        print(znak, end='')

znak = input('Podaj znak: ')
n = int(input('Ile razy? '))

szlaczek(znak, n)
