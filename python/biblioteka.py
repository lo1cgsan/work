#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  biblioteka.py
#
import random


def losujLiczby(lista, ile, maks):
    """
    Funkcja losuje podaną w zmiennej ile ilość liczb
    z zakresu <0, maks>.
    """
    for i in range(ile):
        lista.append(random.randint(0, maks))


def min(tab, n):
    """
    Funkcja wyszukuje najmniejszą liczbę w podanej liście.
    # liczba operacji = n-1
    """
    min = tab[0]
    for i in range(1, n):
        if tab[i] < min:
            min = tab[i]
    return min


def max(tab, n):
    """
    Funkcja wyszukuje największą liczbę w podanej liście.
    # liczba operacji = n-1
    """
    max = tab[0]
    for i in range(1, n):
        if tab[i] > max:
            max = tab[i]
    return max


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
