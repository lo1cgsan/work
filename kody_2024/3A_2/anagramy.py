# anagramy
def sumuj_ASCII(wyraz):
    suma = 0
    for znak in wyraz:
        kod = ord(znak)
        suma = suma + kod
    print(suma)
    return suma

w1 = 'abc'
w2 = 'bac'

w1 = w1.lower().replace(' ', '')
w2 = w2.lower().replace(' ', '')

if sumuj_ASCII(w1) == sumuj_ASCII(w2):
    print('anagramy')
else:
    print('nie anagramy')
