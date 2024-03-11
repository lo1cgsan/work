n = int(input("Podaj liczbę: "))

pierwsza = True

for x in range(2, n):
    if n % x == 0:
        pierwsze = False

if pierwsza:
    print("Liczba pierwsza!")
else:
    print("Nie pierwsza!")



