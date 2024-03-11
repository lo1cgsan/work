# pobierz liczbę całkowitą
o1 = int(input("Podaj liczbę osób: "))
# pobierz liczbę rzeczywistą
s1 = float(input("Podaj ilość składnika: "))
o2 = int(input("Podaj dla ilu osób: "))

if o1 > 0: # pokrywka 1
    print("1 warunek prawdziwy")
    if s1 > 0: # pokrywka 2
        print("2 warunek prawdziwy")
        if o2 > 0: # pokrywka 3
            print("3 warunek prawdziwy")
            s2 = s1 * o2 / o1
            print(s2)
        else: # denko 3
            print("Błędne dane 3!")
    else: # denko 2
        print("Błędne dane 2!")
else: # denko 1
    print("Błędne dane 1!")

