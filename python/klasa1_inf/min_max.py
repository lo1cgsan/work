from random import randint, seed
n = int(input("Ile liczb? "))
liczby = []

seed(234567)
for i in range(n):
    liczby.append(randint(-100, 100))

print(liczby)

min_w = liczby[0]  # inicjacja minimum
max_w = liczby[0]  # inicjacja maksimum

for i in range(1, n):
    liczba = liczby[i]
    if liczba < min_w:
        min_w = liczba
    if liczba > max_w:
        max_w = liczba

print("Min:", min_w, min(liczby))
print("Max:", max_w, max(liczby))
