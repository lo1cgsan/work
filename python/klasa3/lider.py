#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lider.py
#
from random import randint


def generuj_liste(n, zakres):
    lista = []
    w = randint(0, zakres)
    for i in range(n):
        if randint(1, 2) % 2:
            lista.append(randint(0, zakres))
        else:
            lista.append(w)
    return lista


def wyszukaj_lidera(lista, n):
    licz = 0
    for i in range(n):
        if not licz:
            w = lista[i]
            licz = 1
        elif w == lista[i]:
            licz += 1
        else:
            licz -= 1
    return licz, w


def sprawdz_lidera(lista, licz, w, n):
    if not licz:
        t = False
    else:
        licz = 0
        for i in range(n):
            if w == lista[i]:
                licz += 1
        t = licz > n // 2

    if t:
        print(f"{w}: {licz}")
    else:
        print("Brak lidera!")


def main(args):
    n = 80
    lista = generuj_liste(n, 100)
    print(lista)
    licz, w = wyszukaj_lidera(lista, n)
    print(licz, w)
    sprawdz_lidera(lista, licz, w, n)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
