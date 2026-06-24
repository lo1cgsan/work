# Napisz program, który znajduje najmniejszy element z n liczb

# n = 32
liczby = [5, 8, -1, 12, 0, 6, -1, 10]
n = len(liczby)

min_indeks = 0

# przeszukiwanie liniowe
# liczba porównań to n - 1
for i in range(1, n):
    if liczby[i] < liczby[min_indeks]:
        min_indeks = i

print(min_indeks, liczby[min_indeks])
