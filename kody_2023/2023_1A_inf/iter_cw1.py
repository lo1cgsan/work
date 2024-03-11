# iter_cw1.py

# Napisz program, który pobiera i sumuje 5 liczb od użytkownika.
# Wypisz sumę pobranych liczb.

#suma = 0
#for x in range(5):
#    a = int(input("Podaj liczbę: "))
#    suma = suma + a

#print(suma)

# Napisz program, który pobiera od użytkownika 7 liczb
# i wypisuje najmniejszą i największą pobraną liczbę.

# Algorytm znajdowania wartości minimalnej i maksymalnej

l_min = l_max = int(input("Podaj liczbę: "))
for x in range(6):
    a = int(input("Podaj liczbę: "))
    if a < l_min:
        l_min = a
    elif a > l_max:
        l_max = a

print(l_min, l_max)
