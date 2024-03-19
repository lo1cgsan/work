def utworz_konto(imie):
    return {'bilans': 0, 'imie': imie}

def wplata(ile, konto):
    konto['bilans'] += ile
    return konto['bilans']

def wyplata(ile, bilans):
    if bilans > 0:
        bilans -= ile
    else:
        print('Brak środków')
    return bilans

osoba1 = utworz_konto('Alek')
wplata(50, osoba1)
wplata(40, osoba1)
print('Konto:', osoba1['bilans'])

