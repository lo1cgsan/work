# suma_liczb.py
# Napisz program, który pobiera liczby aż ich suma
# przekroczy wartość 75.

suma = 0
licznik = 0
print('Podaj 5 liczb, których suma będzie równa 75!')

while suma < 75:
    liczba = int(input('Podaj liczbę: '))
    suma += liczba
    licznik += 1

print(f'Suma: {suma} Licznik: {licznik}')

if licznik == 5:
    print('Wygrałeś')
else:
    print('Ucz się liczyć dalej')
