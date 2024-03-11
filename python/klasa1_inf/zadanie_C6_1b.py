liczby = []  # zdefiniuj pustą listę o nazwie liczby

liczba = float(input("Podaj liczbę: "))

licznik = 0

while liczba != 0:
    licznik += 1
    liczby.append(liczba)
    liczba = float(input("Podaj liczbę: "))

print(licznik)

for i in range(licznik-1, -1, -2):
    print(i, liczby[i])
    
