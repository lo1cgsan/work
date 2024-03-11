#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Napisz program, któ©y pobiera od użytkownika dwie liczby
#  i drukuje odpowiednie komunikaty, np.
#  "Liczba pierwsza jest większa", "Liczba druga jest większa".
#  "Liczby są równe"

def main(args):
    liczba1 = int(input("Podaj liczbę 1: "))
    liczba2 = int(input("Podaj liczbę 2: "))
    
    if liczba1 > liczba2:
        print("Liczba 1 jest większa")
    elif liczba1 < liczba2:
        print("Liczba 2 jest większa")
    else:
        print("Liczby są równe")

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
