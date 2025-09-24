# Napisz program, który znajduje najmniejszy element z n liczb

# n = 32
liczby = [5, 8, 9, 12, 0, 6, -4, 10]
n = len(liczby)

min_w = liczby[0]
max_w = liczby[0]

# przeszukiwanie liniowe
# liczba porównań to n - 1
for i in range(1, n):
    if min_w > liczby[i]:
        min_w = liczby[i]
    if max_w < liczby[i]:
        max_w = liczby[i]

print(min_w, max_w)
print('Rozpiętość zbioru:', max_w - min_w)
