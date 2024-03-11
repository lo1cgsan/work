# Napisz program "kwadraty2.py", który wyświetla kwadraty kolejnych
# liczb naturalnych z dodatniego przedziału <n,m> określonego
# przez użytkownika.

# Dane wejściowe: n, m – liczby całkowite dodatnie
n = int(input("Podaj n: "))
m = int(input("Podaj m: "))

if n > 0 and m > 0 and n < m:
    for liczba in range(n, m + 1):
        print(liczba**2)
