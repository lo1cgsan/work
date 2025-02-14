# dane wejściowe
n = int(input('Ile wyników: '))
prog = int(input('Próg zaliczenia: '))

for i in range(n):
    lp = int(input('Liczba pytań: '))
    lodp = int(input('Liczba odpowiedzi: '))
    procent = lodp / lp * 100
    print(procent)
    if procent >= prog:
        print('zdał')
    else:
        print('nie zdał')
