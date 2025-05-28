liczby = [6, 5, 3, 1, 8, 7, 2, 4]
n = len(liczby)

for i in range(n-1, 0, -1):
    for j in range(i):
        print(liczby[j], ">", liczby[j+1], end=" ")
        if liczby[j] > liczby[j+1]:
            tmp = liczby[j]
            liczby[j] = liczby[j+1]
            liczby[j+1] = tmp
    print()


print(liczby)
