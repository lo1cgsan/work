# ćwiczenie 9.1/137 z podręcznika
o1 = int(input("Podaj liczbę osób: "))
s1 = float(input("Podaj ilość składnika: "))
o2 = int(input("Podaj dla ilu osób: "))

if o1 > 0 and s1 > 0 and o2 > 0:
    s2 = s1 * o2 / o1
    print("Ilość składnika:", s2)
else:
    print("Błędne dane!")
