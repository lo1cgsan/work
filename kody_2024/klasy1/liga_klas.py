# dane wejściowe
pkt = int(input('Punkty: '))
f = float(input('Frekwencja: '))
so = float(input('Średnia ocen: '))

print(f'Punkty: {pkt}. Frekwencja: {f}. Średnia: {so}.')

# operacje wg algorytmu
if f > 94 and so >= 4:
    pkt = pkt + 20

# dane wyjściowe, wynik
print(f'Punkty: {pkt}.')
