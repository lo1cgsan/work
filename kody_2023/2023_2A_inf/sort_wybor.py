lista = [3, 6, 1, 9, 2, 8, 3, 6, 1, 9, 2, 8]
# lista = list(range(10))
# lista.sort(reverse = True)
n = len(lista)

range(0, n)

def sort_selection(n):
    licznik = 0
    for i in range(n):
        k = i  # ustawiamy indeks najmniejszego elementu
        for j in range(i + 1, n):
            licznik += 1
            if lista[j] < lista[k]:
                k = j
        lista[i], lista[k] = lista[k], lista[i]

    print(n, 2 * licznik)

sort_selection(n)
print(lista)
