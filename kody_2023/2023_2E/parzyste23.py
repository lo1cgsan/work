# Napisz program "parzyste3.py", który wypisuje wszystkie dwucyfrowe
# liczby parzyste podzielne przez 3 w zakresie <n, m>
# podanym przez użytkownika.
# Program powinien sprawdzać poprawność danych wejściowych.

min_w = 10
max_w = 99

n = int(input("Podaj n: "))
m = int(input("Podaj m: "))

if n >= min_w and n <= max_w and m >= min_w and m <= max_w and n < m:
    for liczba in range(n, m + 1):
        if liczba % 2 == 0 and liczba % 3 == 0:
            print(liczba)
