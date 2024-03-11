liczby = []  # zdefiniuj pustą listę o nazwie liczby
n = 5

for i in range(n):
    a = float(input("Podaj liczbę a: "))
    liczby.append(a)

print(liczby)

for i in range(n-1, -1, -1):
    print(i, liczby[i])

liczby.reverse()
print(liczby)
    
