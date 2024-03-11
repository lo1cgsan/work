from random import randint

def losuj(liczby, ile, zakres):
    for i in range(ile):
        liczby.append(randint(0, zakres))

    print(liczby)


def pobierz_typy(typy, ile):
    for i in range(ile):
        typy.append(int(input("Podaj typ: ")))

    print(typy)


def main(args):
    # dane wejściowe
    ile = 10
    ile_typow = 3
    zakres = 10
    liczby = []  # pusta lista
    typy = []
    
    # operacje wykonywane przez program
    losuj(liczby, ile, zakres)  # wywołanie funkcji
    pobierz_typy(typy, ile_typow)
    
    print(set(liczby) & set(typy))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
