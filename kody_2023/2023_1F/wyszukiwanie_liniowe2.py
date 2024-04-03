from random import randint

x = randint(1, 10)
y = randint(1, 10)
z = randint(1, 10)

licznik = 0
for i in range(5):
    a = int(input("Podaj liczbę: "))
    if a == x or a == y or a == z:
        print("Zgadłeś:", a)
        licznik = licznik + 1

print(x, y, z)
print("Liczba odgadniętych:", licznik)












"""
Napisz pętlę, która pobierze 5 liczb z klawiatury
i policzy, ile liczb odgadł użytkownik. Wypisz odgadnięte liczby,
a po pętli wylosowane liczby oraz liczbę odgadniętych.
"""
