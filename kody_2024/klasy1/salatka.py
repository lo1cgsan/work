o1 = int(input('Podaj liczbę osób w przepisie: '))
s1 = float(input('Podaj ilość składnika: '))
o2 = int(input('Dla ilu osób? '))

if o1 > 0 and s1 > 0 and o2 > 0:
    s2 = (s1 * o2) / o1
    print(f'Dla {o2} osób potrzeba {s2} składnika.')
else:
    print('Błędne dane!')
