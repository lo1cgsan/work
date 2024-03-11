# Napisz program, który wypisuje kwadraty kolejnych liczb naturalnych,
# począwszy od zera a skończywszy na kwadracie liczby
# podanej przez użytkownika.
n = int(input("Podaj liczbę: "))

if n >= 0:
    for liczba in range(n + 1):
        print(liczba ** 2)
else:
    print("Błędne dane.")
