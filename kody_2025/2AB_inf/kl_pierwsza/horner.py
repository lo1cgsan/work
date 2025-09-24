n = 3  # stopień wielomainu

l_wsp = []  # lista współczynników
for i in range(n+1):
    w = float(input(f'Podaj współczynnik {i}: '))
    l_wsp.append(w)

x = float(input('Podaj x: '))

wynik = l_wsp[0]
for i in range(1, n+1):
    wynik = wynik * x + l_wsp[i]

print('Wynik:', wynik)
