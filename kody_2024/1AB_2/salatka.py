# dane wejściowe
o1 = int(input('Liczba osób: '))
s1 = float(input('Ilość składnika: '))
o2 = int(input('Liczba osób: '))

if o1 > 0 and s1 > 0 and o2 > 0:
    s2 = s1 * o2 / o1
    print(f'Potrzeba {s2} składnika.')
else:
    print('Błędne dane!')
