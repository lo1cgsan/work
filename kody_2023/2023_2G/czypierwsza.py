def czy_pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = int(input('Podaj liczbę: '))
if czy_pierwsza(n):
    print('pierwsza')
else:
    print('nie pierwsza')
