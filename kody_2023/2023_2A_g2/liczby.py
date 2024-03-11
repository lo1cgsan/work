# pobierz liczbę całkowitą
# a = int(input("Pobierz liczbę: "))

# pobierz liczbę rzeczywistą
a = float(input("Podaj liczbę: "))
b = float(input("Podaj liczbę: "))

pole = a * b
obwod = 2 * (a + b)

print(pole, obwod)

print(f"Pole: {round(pole, 2)} Obwód: {round(obwod, 2)}")


if a > b:
    print("a > b")
elif a < b:
    print("a < b")
else:
    print("a == b")

# for i in "abrakadabra":
# for i in 1,2,3,4,5:
for i in range(1, 11):
    # wypisz tylko liczby nieparzyste
    if i % 2 == 1:
        print(i)





