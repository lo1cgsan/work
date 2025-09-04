# dane wejściowe
n = int(input('Liczba wyników: '))

for _ in range(n):
    l_pyt = int(input('Liczba pytań: '))
    l_odp = int(input('Dobre odpowiedzi: '))
    prog = int(input('Próg: '))  # próg zaliczenia

    # operacje (algorytm)
    procent = l_odp / l_pyt * 100
    print(procent)

    # dane wyjściowe, wynik
    if procent >= prog:
        print("zdał")
    else:
        print("nie zdał")
