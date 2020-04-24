#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def losujLiczby(lista, n, maks):
    for i in range(n):
        lista.append(random.randint(0, maks))


def get_min(lista):
    # n-1
    l_min = lista[0]
    for liczba in lista:
        if liczba < l_min:
            l_min = liczba
    return l_min


def get_max(lista):
    l_max = lista[0]
    for liczba in lista:
        if liczba > l_max:
            l_max = liczba
    return l_max

# n-1 + n-2 = 2n - 3 (10 => 17) (10000 => 19997)
# n/2 + n/2-1 + n/2-1 = 3n/2 - 2 (10 => 13) (10000 => 14998)


def main(args):
    lista = []  # pusta lista
    n = int(input("Podaj ilość liczb: "))
    maks = 50
    losujLiczby(lista, n, maks)
    print(lista)
    l_min = get_min(lista)
    l_max = get_max(lista)
    print(l_min, " ", l_max)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
