# anagramy
def sumuj_ASCII(wyraz):
    suma = 0
    for znak in wyraz:
        kod = ord(znak)
        suma = suma + kod
    return suma

w1 = input('Podaj wyraz: ')
w2 = input('Podaj wyraz: ')

w1 = w1.lower().replace(' ', '')
w2 = w2.lower().replace(' ', '')

if sumuj_ASCII(w1) == sumuj_ASCII(w2):
    print("Anagramy")
else:
    print("Nie anagramy")
