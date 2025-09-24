# Napisz program, który wypisuje liczby
# parzyste od 0 do 100. Policz i wypisz,
# ile jest takich liczb.

# wersja 1
licznik = 0

for i in range(1, 101):
    if i % 2 == 0:
        print(i)
        licznik = licznik + 1

print(licznik)

print('wersja 2')
liczba = 0
licznik = 0
for i in range(50):
    liczba += 2
    print(liczba)
    licznik += 1
print(licznik)


print('wersja 3')
lista = range(2, 101, 2)
for i in lista:
    print(i)
print(len(lista))
