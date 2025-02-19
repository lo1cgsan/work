# suma_liczb2.py
# pobieraj liczby, aż ich suma wyniesie 75

i = 1
suma = 0

while suma < 75:
    liczba = int(input(f'Podaj liczbę {i}: '))
    i = i + 1
    suma = suma + liczba

print(f'Suma liczb: {suma}')
