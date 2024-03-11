#!/usr/bin/env python
# -*- coding: utf-8 -*-

class KontoBasic():
    def __init__(self, ile=0, dane={}):
        self.bilans = ile
        self.osoba = dane
        
    def wplata(self, ile):
        self.bilans += int(ile)
        return self.bilans
        
    def wyplata(self, ile):
        self.bilans -= int(ile)
        return self.bilans


class KontoPremium(KontoBasic):
    def __init__(self, ile=0, dane={}, debet=0):
        super().__init__(ile, dane)
        self.debet = debet

    def wyplata(self, ile):
        if self.bilans - int(ile) < self.debet:
            print("Brak środków!")
            return self.bilans
        else:
            return super().wyplata(ile)


konta = [
    KontoBasic(100, {'imie': 'Ala', 'nazwisko': 'Kot'}),
    KontoPremium(100, {'imie': 'Ela', 'nazwisko': 'Pies'}, -50),
]

kto = input('Imię: ')
klient = None
for k in konta:
    if k.osoba['imie'] == kto:
        klient = k

while True:
    op = input('Operacja: ').strip()
    if op == '+':
        ile = input('Wpłata: ')
        klient.wplata(ile)
    elif op == '-':
        ile = input('Wypłata: ')
        klient.wyplata(ile)
    else:
        break
    print('Konto:', klient.bilans)
