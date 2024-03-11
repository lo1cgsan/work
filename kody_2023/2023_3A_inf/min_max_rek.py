def min_max_rek(i, j):
    
    if i == j:  # zbiór 1-elementowy
        min_w, max_w = i, j
    if i + 1 == j:  # zbiór 2-elementowy
        if lista[i] >= lista[j]:
            min_w, max_w = j, i
        else:
            min_w, max_w = i, j
        print("w10:", i, j, lista[i], lista[j], min_w, max_w)
    else:  # zbiór > 2-elementowy
        k = (i + j) // 2
        min1, max1 = min_max_rek(i, k)
        print("w14:", i, k, lista[min1], lista[max1])
        min2, max2 = min_max_rek(k+1, j)
        print("w16:", k+1, j, lista[min2], lista[max2])
        
        if lista[min1] <= lista[min2]:
            min_w = min1
        else:
            min_w = min2
        
        if lista[max1] >= lista[max2]:
            max_w = max1
        else:
            max_w = max2

    return min_w, max_w


lista = [1, 4, 3, 2, 4, 9, 5, 7]
m1, m2 = min_max_rek(0, len(lista) - 1)
print(lista[m1], lista[m2])
