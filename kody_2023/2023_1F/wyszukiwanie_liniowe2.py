from random import randint

x = randint(1, 10)

for i in range(10):
    y = randint(1, 10)
    if y != x:
        break  # przerwij pętlę

for i in range(10):
    z = randint(1, 10)
    if z != x and z != y:
        break  # przerwij pętlę

print(x, y, z)

licznik = 0
for i in range(3):
    a = int(input("Podaj liczbę: "))
    if a == x or a == y or a == z:
        print("Zgadłeś:", a)
        licznik = licznik + 1

print(x, y, z)
print("Liczba odgadniętych:", licznik)
