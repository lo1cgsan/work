from random import randint, seed

x = randint(1, 10)
y = randint(1, 10)
z = randint(1, 10)

"""
Napisz pętlę, która pobierze 5 liczb z klawiatury
i policzy, ile liczb odgadł użytkownik. Wypisz odgadnięte liczby,
a po pętli wylosowane liczby oraz liczbę odgadniętych.
"""
for i in range(5):
    a = int(input("Podaj liczbę: "))
    if a == x:
        print("Zgadłeś:", a)
    if a == y:
        print("Zgadłeś:", a)
    if a == z:
        print("Zgadłeś:", a)

print(x, y, z)
