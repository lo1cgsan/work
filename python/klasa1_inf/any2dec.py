def horner_it(st, lwsp, x):
    """
            0, 1, 2, 3
    lwsp = [3, 2, 1, 4]
    
    x * (x * (a0 * x + a1) + a2) + a3
    """
    wynik = lwsp[0]
    for i in range(1, st + 1):
        wynik = wynik * x + lwsp[i]
    return wynik

stopien = int(input("Ile cyfr? "))
x = float(input("Podaj podstawę: "))
lista_wsp = []

for i in range(stopien + 1):
    w = float(input(f"Podaj cyfrę {i}: "))
    lista_wsp.append(w)

print(x, lista_wsp)
print("Wynik:", horner_it(stopien, lista_wsp, x))

# 1*2^2 + 1*2 + 1 = 7
# 10011(2)
# 1*2^4 + 0*2^3 + 0*2^2 + 1*2^1 + 1*2^0

# 123(10) = 1 * 10^2 + 2 * 10^1 + 3 * 10^0
st = 3
0 - 9, A, B, C, D, E, F
FFC0(16) = 

