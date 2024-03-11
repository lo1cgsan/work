def min_e(lista):
    # algorytm wyszukiwania liniowego
    n = len(lista)
    min_w = lista[0]
    for i in range(1, n):
        if lista[i] < min_w:
            min_w = lista[i]

    print(min_w)

def max_e(lista):
    # algorytm wyszukiwania liniowego
    n = len(lista)
    max_w = lista[0]
    for i in range(1, n):
        if lista[i] > max_w:
            max_w = lista[i]

    print(max_w)
# min_e() = n - 1, max_e() = n - 1, w sumie 2n - 2 operacje

lista = [3, 6, 1, 9, 2, 8, 3, 6, 1, 9, 2, 8]
n = len(lista)

z_min = []  # liczby mniejsze
z_max = []  # liczby większe

# n / 2
for i in range(0, n, 2):
    if lista[i] < lista[i+1]:
        z_min.append(lista[i])
        z_max.append(lista[i+1])
    else:
        z_min.append(lista[i+1])
        z_max.append(lista[i])

# n / 2 - 1
print(z_min)
min_e(z_min)

# n / 2 - 1
print(z_max)
max_e(z_max)

# n / 2 + n / 2 - 1 + n / 2 - 1 = 3n/2 - 2
