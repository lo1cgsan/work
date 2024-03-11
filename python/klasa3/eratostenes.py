#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  eratostenes.py
import math


def czy_pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            print(i)
            return False
    return True


def sito_eratostenesa(n):
    lista = [True] * (n + 1)
    for i in range(2, int(math.sqrt(n))):
        if lista[i]:
            j = i + i
            while j <= n:
                lista[j] = False
                j = j + i

    for i in range(2, n + 1):
        if lista[i]:
            print(i, " ", end="")
    print(lista.count(True) - 2)


def main(args):
    n = int(input("Podaj liczbę: "))
    # ~if czy_pierwsza(n):
    # ~print("Pierwsza!")
    # ~else:
    # ~print("Nie jest pierwsza!")
    sito_eratostenesa(n)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
