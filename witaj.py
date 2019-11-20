#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    # print("Witaj!")
    imie = input("Podaj imię: ")
    print("Witaj,", imie+"!")
    
    wiek = int(input("Podaj wiek: "))
    
    rok_aktualny = 2019
    rok_pythona = 1992
    wiek_pythona = rok_aktualny - rok_pythona
    # INSTRUKCJA WARUNKOWA
    if wiek > wiek_pythona:
        print("Jesteś starszy")
    elif wiek < wiek_pythona:
        print("Jesteś młodszy")
    else:
        print("Mamy tyle samo lat!")

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
