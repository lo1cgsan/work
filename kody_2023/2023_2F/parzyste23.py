# Napisz program "parzyste3.py", który wypisuje wszystkie dwucyfrowe
# liczby parzyste podzielne przez 3 w zakresie <n, m> podanym przez użytkownika.
# Program powinien sprawdzać poprawność danych wejściowych.

n = int(input("Podaj liczbę: "))
m = int(input("Podaj liczbę: "))

if n >= 100 and n <= 999 and m >= 100 and m <= 999 and n < m:
    licznik = 0
    for liczba in range(n, m + 1):
        if liczba % 2 == 0 and liczba % 3 == 0:
            print(liczba)
            licznik = licznik + 1
    print("Licznik:", licznik)
else:
    print("Błędne dane!")
