lng = int(input("Podaj liczbę nadgodzin: "))
s = float(input("Podaj stawkę nadgodzin: "))

if lng <= 30:
    placa = lng * s
else:
    placa = lng * s + (lng - 30) * s * 0.5

print(placa)
