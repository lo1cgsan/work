def sort_insert(l, n):
    for i in range(1, n):
        el = l[i]
        j = i - 1
        while j > -1 and l[j] > el:
            l[j + 1] = l[j]
            j = j - 1
        l[j + 1] = el

dane = [6, 5, 3, 1, 8, 7, 2, 4]
n = len(dane)
sort_insert(dane, n)
print(dane)
