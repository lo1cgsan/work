def min_e(lista):
    """
    Liniowe wyszukiwanie wartości minimalnej.
    Złożoność: O(n) = n - 1 operacji porównania.
    """
    min_w = lista[0]
    n = len(lista)
    for i in range(1, n):
        if lista[i] < min_w:
            min_w = lista[i]

    return min_w


def max_e(lista):
    """
    Liniowe wyszukiwanie wartości maksymalnej.
    Złożoność: O(n) = n - 1 operacji porównania.
    """
    max_w = lista[0]
    n = len(lista)
    for i in range(1, n):
        if lista[i] > max_w:
            max_w = lista[i]

    return max_w


def rozpietosc(lista):
    """
    Złożoność: n - 1 + n - 1 = 2n - 2
    """
    return max_e(lista) - min_e(lista)


def min_maks(lista):
    """
    Jednoczesne wyszukiwanie liniowe wartości min i maks
    Złożoność: n/2 + n/2 - 1 + n/2 -1 = 3n/2 - 2
    """
    z_min = []
    z_max = []

    n = len(lista)
    for i in range(0, n, 2):
        if lista[i] < lista[i+1]:
            z_min.append(lista[i])
            z_max.append(lista[i+1])
        else:
            z_min.append(lista[i+1])
            z_max.append(lista[i])

    min_w = min_e(z_min)
    max_w = max_e(z_max)

    return min_w, max_w

lista = [3, 6, 1, 9, 2, 8, 3, 6, 1, 9, 2, 8]
print(min_e(lista))
print(max_e(lista))
# n-1 + n-1 = 2n - 2
print(min_maks(lista))
# 3n/2 - 2
