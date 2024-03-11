lista = [3, 6, 1, 9, 2, 8, 3, 6, 1, 9, 2, 8]
lista = list(range(10))
# lista.sort(reverse = True)
n = len(lista)

def babelkowe():
    licznik = 0
    licznik2 = 0
    for i in range(n - 1, 0, -1):
        for j in range(i):
            print(lista[j], " > ", lista[j + 1])
            licznik += 1
            if lista[j] > lista[j+1]:
                licznik2 += 1
                tmp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = tmp

# n = 6  F(n) = 15
# n = 12 F(n) = 60

    print(n, licznik)
    print(n, licznik2)

babelkowe()
print()
print(lista)
print()

# [3, 6, 1, 9, 2, 8]
# [3, 1, 6, 9, 2, 8]
# [3, 1, 6, 2, 9, 8]
# [3, 1, 6, 2, 8, 9]
# [1, 3, 6, 2, 8, 9]
# [1, 3, 2, 6, 8, 9]
