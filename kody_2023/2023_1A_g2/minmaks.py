"""
Napisz program, który pobiera od użytkownika n liczb
i wypisuje największą oraz najmniejszą z nich.
Pobierz n od użytkownika.
"""
n = int(input("Ile liczb: "))

min_w = int(input("Podaj liczbę: "))
max_w = min_w

for i in range(n-1):
    a = int(input("Podaj liczbę: "))
    if a < min_w:
        min_w = a
    if a > max_w:
        max_w = a

print(min_w)
print(max_w)
