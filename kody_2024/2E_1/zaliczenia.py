# dane wejściowe
prog = 80
n = int(input('Liczba wyników: '))

for i in range(n):
    l_pyt = int(input('Liczba pytań: '))
    l_odp = int(input('Liczba odpowiedzi: '))

    # operacje wg algorytmu
    procent = l_odp / l_pyt * 100

    # wynik, dane wyjściowe
    if procent >= prog:
        print('zdał')
    else:
        print('nie zdał')
