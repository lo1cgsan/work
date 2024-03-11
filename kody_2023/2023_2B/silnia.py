# dane wejściowe
n = int(input("Podaj liczbę: "))

wynik = 1

for i in range(1, n+1):
    print(wynik, "*", i)
    wynik = wynik * i

print(wynik)
