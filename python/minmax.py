#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def losujLiczby(lista, n, maks):
    for i in range(n):
        lista.append(random.randint(0, maks))


def get_min(lista):
    l_min = lista[0]
    for liczba in lista:
        if liczba < l_min:
            l_min = liczba
    return l_min


def main(args):
    lista = []  # pusta lista
    n = int(input("Podaj ilość liczb: "))
    maks = 50
    losujLiczby(lista, n, maks)
    print(lista)
    l_min = get_min(lista)
    print(l_min)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
