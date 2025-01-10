def sumuj_ASCII(wyraz):
    suma = 0
    for znak in wyraz:
        kod = ord(znak)  # kod ASCII
        suma = suma + kod
    return suma

w1 = 'abc'
w2 = 'bac'

w1 = w1.lower().replace(' ', '')
w2 = w2.lower().replace(' ', '')

if sumuj_ASCII(w1) == sumuj_ASCII(w2):
    print('Anagramy')
else:
    print('Nie anagramy')
