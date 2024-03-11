#!/usr/bin/env python
# -*- coding: utf-8 -*-

bilans = 0

while True:
    op = input('Operacja: ').strip()
    if op == '+':
        ile = input('Wpłata: ')
        bilans += int(ile)
    elif op == '-':
        ile = input('Wypłata: ')
        bilans -= int(ile)
    else:
        break
    print('Konto:', bilans)
