# Napisz program, który wyszukuje jednocześnie element minimalny i maksymalny
# przy użyciu metody dziel i zwyciężaj

liczby = [5, 8, -1, 12, 0, 6, -1, 10, 16]
n = len(liczby)
ostatni = None
if n % 2 == 1:
    ostatni = liczby[n-1]
    n = n - 1

mniejsze = []
wieksze = []

# n/2 porównań par elementów
for i in range(0, n, 2):
    if liczby[i] > liczby[i+1]:
        wieksze.append(liczby[i])
        mniejsze.append(liczby[i+1])
    else:
        wieksze.append(liczby[i+1])
        mniejsze.append(liczby[i])

min_w = mniejsze[0]
max_w = wieksze[0]

# przeszukiwanie liniowe, liczba porównań to n/2 - 1
for i in range(1, n//2):
    if min_w > mniejsze[i]:
        min_w = mniejsze[i]
    if max_w < wieksze[i]:
        max_w = wieksze[i]

if ostatni:
    if ostatni < min_w:
        min_w = ostatni
    elif ostatni > max_w:
        max_w = ostatni

print(min_w, max_w)
