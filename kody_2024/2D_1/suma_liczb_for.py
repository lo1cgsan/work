# suma_liczb.py

n = int(input('Ile liczb? '))

suma = 0
for i in range(n):
    liczba = int(input(f'Podaj liczbę {i+1}: '))
    suma = suma + liczba

print(f'Suma liczb: {suma}')
