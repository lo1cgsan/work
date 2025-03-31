# salatka.py
# dane wejściowe
o1 = int(input('Liczba osób o1: '))
s1 = float(input('Ilość składnika s1: '))
o2 = int(input('Liczba osób o2: '))

if o1 > 0 and s1 > 0 and o2 > 0:
    # obliczenia
    s2 = s1 * o2 / o1

    # wynik
    print(s2)
else:
    print('Błędne dane!')
