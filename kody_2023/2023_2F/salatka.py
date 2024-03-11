o1 = int(input("Podaj liczbę osób: "))
s1 = float(input("Podaj ilość składnika: "))
o2 = int(input("Dla ilu osób? "))

if o1 > 0 and s1 > 0 and o2 > 0:
    s2 = s1 * o2 / o1
    print(s2)
else:
    print("Błędne dane!")

# o1 = 4
# s1 = 15
# o2 = 6
