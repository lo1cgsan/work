#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minmax.py
#
import random


def losujLiczby(lista, ile, maks):
    for i in range(ile):
        lista.append(random.randint(0, maks))


def min(tab, n):
    # liczba operacji = n-1
    min = tab[0]
    for i in range(1, n):
        if tab[i] < min:
            min = tab[i]
    return min


def max(tab, n):
    # liczba operacji = n-1
    max = tab[0]
    for i in range(1, n):
        if tab[i] > max:
            max = tab[i]
    return max


def minmax(tb, n):
    """
    Funkcja odczytuje z przekazanej listy po dwie liczby i je porównuje.
    Mniejsze dodawane są do listy tbmin, większe do listy tbmax.
    Funkcja zwraca listy liczb mniejszych i większych.
    """
    tbmin = []
    tbmax = []
    i = 0
    for i in range(0, n - 1, 2):
        print(tb[i], tb[i + 1])
        if tb[i] <= tb[i + 1]:
            tbmin.append(tb[i])
            tbmax.append(tb[i + 1])
        else:
            tbmax.append(tb[i])
            tbmin.append(tb[i + 1])
    if n % 2:  # lista zawiera nieparzystą ilość liczb
        print(tb[i + 2], tb[i + 1])
        if tb[i + 2] < tb[i + 1]:
            tbmin.append(tb[i + 2])
        else:
            tbmax.append(tb[i + 2])
    print(f"Liczby mniejsze: {tbmin}\nLiczby większe: {tbmax}")
    return tbmin, tbmax


def main(args):
    tab = []  # pusta lista
    n = int(input("Ile liczb? "))
    MAKS = 50
    losujLiczby(tab, n, MAKS)
    print("Wylosowane liczby:\n", tab)

    tbmin, tbmax = minmax(tab, n)
    min_el = min(tbmin, len(tbmin))
    max_el = max(tbmax, len(tbmax))
    print(f"Minimum: {min_el}. Maksimum: {max_el}.")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
