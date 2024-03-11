#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cena_komputera.py
#  

def main(args):
    cenak = int(input("Podaj cenę komputera: "))
    print("Cena wyjściowa:", cenak)
    cenap = int(input("Podaj cenę płyty: "))
    w = input("Podaj procent podwyżki: ")
    # =JEŻELI(C2<=10%;A2;
    if int(w) <= 10:
        print("Cena komputera:", cenak)
    # JEŻELI(C2<=20%;A2+0,05*(B2+C2*B2);
    elif int(w) <= 20:
        cenak = cenak + 0.05 * (cenap + int(w) * cenap / 100)
        print("Cena komputera:", cenak)
    else:  # "za wysoka cena"))
        print("Za wysoka cena")
    

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
