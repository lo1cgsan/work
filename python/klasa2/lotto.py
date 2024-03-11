from random import randint


def losuj(ile, zakres):
    liczby = []  # definicja pustej listy
    for i in range(ile):
        liczba = randint(0, zakres)
        liczby.append(liczba)
    
    for i in range(3):
        typ = int(input("Podaj typ: "))
        if typ in liczby:
            print("Trafiłeś!")
        else:
            print("Niestety!")

    print(liczby)
    

def main():
    ile = int(input("Ile liczb wylosować? "))
    zakres = int(input("Podaj zakres? "))
    losuj(ile, zakres)
    return 0


main()
