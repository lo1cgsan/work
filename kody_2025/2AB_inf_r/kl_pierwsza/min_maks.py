from random import randint

liczby = []  # utworzenie pustej listy
n = 10

for i in range(n):
    a = randint(0, 100)
    liczby.append(a)

print(liczby)

min_l = liczby[0]
max_l = liczby[0]

# wyszukiwanie liniowe
for i in  range(1, n):
    el = liczby[i]
    print(el)
    if el > max_l:
        max_l = el
    elif el < min_l:
        min_l = el

# liczba porównań <= 2 * (n - 1)
# O(n) – złożoność liniowa

print("Min:", min_l)
print("Maks:", max_l)
