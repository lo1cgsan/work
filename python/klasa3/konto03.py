#!/usr/bin/env python
# -*- coding: utf-8 -*-

bilans = 0

def wplata(bilans):
    bilans += int(ile)
    
def wyplata(bilans):
    bilans -= int(ile)

while True:
    op = input('Operacja: ').strip()
    if op == '+':
        ile = input('Wpłata: ')
        wplata(bilans)
    elif op == '-':
        ile = input('Wypłata: ')
        wyplata(bilans)
    else:
        break
    print('Konto:', bilans)
