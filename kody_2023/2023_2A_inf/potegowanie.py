def decToBin(liczba, p=2):
    lbin = []
    while liczba != 0:
        lbin.append(liczba % p)
        liczba = liczba // p
    lbin.reverse()
    return lbin

x = float(input("Podaj podstawę: "))
k = int(input("Podaj wykładnik: "))
k = decToBin(k)
print(k)

p = x
for i in range(1, len(k)):
    print(i)
    if k[i] == 1:
        p = p * p * x
    else:
        p = p * p

print(f"{x}^{k} =", p)

# 1010(2) = 10
