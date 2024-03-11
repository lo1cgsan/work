# pobierz liczbę całkowitą
o1 = int(input("Podaj liczbę osób: "))
# pobierz liczbę rzeczywistą
s1 = float(input("Podaj ilość składnika: "))
o2 = int(input("Podaj dla ilu osób: "))

if o1 > 0 and s1 > 0 and o2 > 0:
    s2 = s1 * o2 / o1
    print(s2)
else:
    print("Błędne dane!")


if o1 < 0 or s1 < 0 or o2 < 0:
    print("Błędne dane!")
else:
    s2 = s1 * o2 / o1
    print(s2)    
