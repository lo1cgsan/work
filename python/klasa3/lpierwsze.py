#!/usr/bin/env python
# -*- coding: utf-8 -*-

def lpierwsze(n):
    for i in range(2, n):
        pierwsza = True
        j = 2
        while pierwsza and j < i:
            if i % j == 0:
                pierwsza = False
            j += 1
        if pierwsza:
            print(i)


def sito(n):
    tablica = [True] * n
    for i in range(2, n):
        if tablica[i]:
            j = i + i
            while j < n:
                tablica[j] = False
                j += i

    for i in range(2, n):
        if tablica[i]:
            print(i, " ", end="")


def main(args):
    n = int(input("Podaj liczbę: "))
    # lpierwsze(n)
    sito(n)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
