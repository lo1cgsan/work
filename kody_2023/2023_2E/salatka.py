# ćwiczenie 9.1/137 z podręcznika
o1 = int(input("Podaj liczbę osób: "))
s1 = float(input("Podaj ilość składnika: "))
o2 = int(input("Podaj dla ilu osób: "))

if o1 > 0:
    print("1 warunek prawdziwy")
    if s1 > 0:
        print("2 warunek prawdziwy")
        if o2 > 0:
            s2 = s1 * o2 / o1
            print("Ilość składnika:", s2)
        else:
            print("Błędne dane!")
    else:
        print("Błędne dane!")
else:
    print("Błędne dane!")

