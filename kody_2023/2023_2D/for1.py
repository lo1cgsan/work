# Napisz program, który pobiera z klawiatury liczbę całkowitą n,
# a następnie przy użyciu funkcji suma() sumuje wszystkie liczby
# od 1 do n i zwraca wynik. Program powinien wypisać obliczoną sumę.

# definicja funkcji suma()
def suma(n):
    wynik = 0
    for i in range(1, n + 1):
        wynik = wynik + i

    return wynik

# pobierz n
n = int(input("Podaj n: "))

print(suma(n))
