#!/usr/bin/env python
# -*- coding: utf-8 -*-

def utworzKonto(imie, ile):
    return {'kto': imie, 'bilans': ile}

def wplata(klient):
    klient['bilans'] += int(ile)
    
def wyplata(klient):
    klient['bilans'] -= int(ile)

konta = [utworzKonto('Ala', 0), utworzKonto('Ela', 50)]
kto = input('Imię: ')
klient = None
for k in konta:
    if k['kto'] == kto:
        klient = k

while True:
    op = input('Operacja: ').strip()
    if op == '+':
        ile = input('Wpłata: ')
        wplata(klient)
    elif op == '-':
        ile = input('Wypłata: ')
        wyplata(klient)
    else:
        break
    print('Konto:', klient['bilans'])
