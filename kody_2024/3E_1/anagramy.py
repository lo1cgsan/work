def pobierz_wyraz():
    w = input('Podaj wyraz: ')
    return w.strip().replace(' ', '').lower()

def sumuj_ASCII(tekst):
    suma = 0
    for znak in tekst:
        kod = ord(znak)
        suma = suma + kod
    return suma

w1 = pobierz_wyraz()
w2 = pobierz_wyraz()

print(w1, w2)

if sumuj_ASCII(w1) == sumuj_ASCII(w2):
    print('To anagramy')
else:
    print('To nie anagramy!')
