# Napisz program który pobiera podaną przez użytkownika
# liczbę ocen semestralnych, a następnie oblicza i wypisuje
# ich średnią.
# Dane: n – liczba całkowita, liczba podawanych ocen
#

n = int(input("Ile szminek kupiłaś? "))
torebka = 0

for i in range(n):
    szminka = int(input("Podaj cenę szminki: "))
    torebka = torebka + szminka

print("Srednia ocen:", torebka / n)
