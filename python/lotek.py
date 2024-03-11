#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lotek.py
import random

def losuj(ile, maksliczba):
    liczby = []  # lista
    for i in range(ile):
        liczba = random.randint(1, maksliczba)
        if liczba in liczby:
            pass
        else:
            liczby.append(liczba)
        # print(liczba)
    print(liczby)


def losuj2(ile, maksliczba):
    liczby = []
    while ile > 0:
        # print(ile)
        liczba = random.randint(1, maksliczba)
        if liczba not in liczby:
            liczby.append(liczba)
            ile = ile - 1

    # print(liczby)
    return liczby


def pobierz_typy(ile, maksliczba):
    typy = []
    while ile > 0:
        # print(ile)
        liczba = int(input('Podaj typ: '))
        if liczba not in typy:
            typy.append(liczba)
            ile = ile - 1

    # print(typy)
    return typy


def main(args):
    ile = int(input("Ile liczb typujesz? "))
    maksliczba = int(input("Podaj liczbę maksymalną: "))
    
    liczby = losuj2(ile, maksliczba)
    typy = pobierz_typy(ile, maksliczba)
    trafione = set(liczby) & set(typy)
    if trafione:
        print("Ilość trafień:", len(trafione))
        print("Trafione liczby:", trafione)
    else:
        print("Brak trafień!")
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
