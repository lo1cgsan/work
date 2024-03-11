lista = [3, 6, 1, 9, 2, 8, 3, 6, 1, 9, 2, 8]
lista = list(range(10))
lista.sort(reverse = True)
n = len(lista)

def sort_insert(n):
    licznik = 0
    for i in range(1, n):
        element = lista[i]
        j = i - 1
        while j > -1 and lista[j] > element:
            licznik += 1
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = element
    
    print(2 * licznik)
    
# n = 6  F(n) = 12
# n = 12 F(n) = 54

sort_insert(n)
print(lista)
