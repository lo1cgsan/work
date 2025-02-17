# dane wejściowe
n = int(input('Liczba wyników: '))

for _ in range(n):
    prog = int(input('Próg: '))
    l_pyt = int(input('Liczba pytań: '))
    l_odp = int(input('Liczba odpowiedzi: '))

    # operacje wg algorytmu
    procent = l_odp / l_pyt * 100
    print(procent)

    # dane wyjściowe, wynik
    if procent >= prog:
        print("zdał")
    else:
        print("nie zdał")
