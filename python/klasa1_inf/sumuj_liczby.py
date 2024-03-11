n = int(input("Podaj liczbę od: "))
m = int(input("Podaj liczbę do: "))
suma = 0
for liczba in range(n, m+1):
    print(suma, "+", liczba)
    suma = suma + liczba
print(suma)
