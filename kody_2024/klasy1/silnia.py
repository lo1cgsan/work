n = int(input('Podaj liczbę naturalną: '))

if n >= 0:
    wynik = 1
    for i in range(1, n+1):
        print(f'{wynik} * {i}')
        wynik = wynik * i

    print(f'{n}! = {wynik}')
