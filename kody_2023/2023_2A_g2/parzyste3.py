# Napisz program "parzyste3.py", który wypisuje wszystkie
# dwucyfrowe liczby parzyste podzielne przez 3
# w zakresie <n, m> podanym przez użytkownika.
# Program powinien sprawdzać poprawność danych wejściowych
# i wypisywać liczbę takich liczb.

n = int(input("Podaj n: "))
m = int(input("Podaj m: "))

licznik = 0

if n >= 10 and n <= 99 and m >= 10 and m <= 99 and n < m:
    for liczba in range(n, m + 1):
        if liczba % 2 == 0 and liczba % 3 == 0:
            print(liczba)
            licznik = licznik + 1
    print("Licznik:", licznik)
else:
    print("Błędne dane!")

