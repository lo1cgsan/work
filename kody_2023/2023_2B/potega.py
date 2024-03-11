# dane wejściowe
a = int(input("Podaj podstawę: "))
n = int(input("Podaj wykładnik: "))

#2^4
#1 * 2 = 2
#2 * 2 = 4
#4 * 2 = 8
#8 * 2 = 16

wynik = 1
for i in range(n):
    wynik = wynik * a

print(wynik)
