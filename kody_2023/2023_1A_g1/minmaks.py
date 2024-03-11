"""
Pobierz n od użytkownika.
Napisz program, który pobiera od użytkownika n liczb.

Program powinien wypisać najmniejszą i największą
z podanych liczb.
"""
n = int(input("Ile podasz liczb: "))

min_w = int(input("Podaj liczbę: "))
max_w = min_w

for i in range(n-1):
    liczba = int(input("Podaj liczbę: "))
    if liczba < min_w:
        min_w = liczba
    if liczba > max_w:
        max_w = liczba

print(min_w)
print(max_w)
