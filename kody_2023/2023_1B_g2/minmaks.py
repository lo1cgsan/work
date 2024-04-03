"""
Napisz program, który pobiera od użytkownika
5 liczb i wypisuje najmniejszą i największą.
"""
najmniejsza = int(input("Podaj liczbę: "))
najwieksza = najmniejsza

for i in range(4):
    liczba = int(input("Podaj liczbę: "))
    if liczba < najmniejsza:
        najmniejsza = liczba
    elif liczba > najwieksza:
        najwieksza = liczba

print(najmniejsza, najwieksza)

