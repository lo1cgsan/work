#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  najczesciej.py
#  
from random import randint

def generuj_liste(n):
	lista = []
	for i in range(n):
		lista.append(randint(1, n))	
	return(lista)


def policz_elementy(lista, n):
    max_el = 0
    najczestsza = 0
    badany_el = 0
    for i in range(n):
        badany_el = 0
        for j in range(n):
            if lista[j] == i:
                badany_el += 1
        if max_el < badany_el:
            max_el = badany_el
            najczestsza = i

    print(najczestsza, max_el)


def policz_elementy2(lista, n):
    wystapienia = dict()
    max_el = 0
    najczestsza = 0
    badany_el = 0
    for i in lista:
        badany_el = 0
        if i not in wystapienia:
            for j in range(n):
                if lista[j] == i:
                    badany_el += 1
            if max_el < badany_el:
                max_el = badany_el
                najczestsza = i
            wystapienia[i] = badany_el

    print(najczestsza, max_el)
    print(wystapienia)

    
def main(args):
    ile = 20
    lista = generuj_liste(20)
    print(sorted(lista))
    policz_elementy2(lista, ile)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
