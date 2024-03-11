# Napisz program, który wczytuje z klawiatury poprawny numer miesiąca,
# tzn. liczbę z przedziału <1,12> i wpypisuje nazwę miesiąca.
# Zakładamy, że możliwe są tylko 3 próby podania poprawnego numeru.

powtórz 3 razy:
    m = int(input("Podaj numer miesiąca: "))
    if m == 1:
        print("styczeń")
    elif m == 2:
        print("luty")
    elif m == 3:    
        print("marzec")
    elif m == 4:    
        print("kwiecień")
    elif m == 5:    
        print("maj")
        break
    else:
        print("Błędne dane!")

