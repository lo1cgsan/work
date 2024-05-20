def czy_pierwsza(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

n = int(input('Podaj liczbę: '))
if czy_pierwsza(n) == True:
    print('pierwsza')
else:
    print('nie pierwsza')
