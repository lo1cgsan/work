n = int(input('Podaj liczbę: '))

for i in range(2, n):
    if n % i == 0:
        print('nie pierwsza')
        exit()

print('pierwsza')
