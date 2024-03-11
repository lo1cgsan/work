o1 = int(input("Podaj liczbę osób: "))
s1 = float(input("Podaj ilość składnika: "))
o2 = int(input("Dla ilu osób: "))

if o1 > 0:
    print("1 warunek prawdziwy")
    if s1 > 0:
        print("2 warunek prawdziwy")
        if o2 > 0:
            print("3 warunek prawdziwy")
            s2 = s1 * o2 / o1
            print(s2)
        else:
            print("Błędne dane 3!")
    else:
        print("Błędne dane 2!")
else:
    print("Błędne dane 1!")

