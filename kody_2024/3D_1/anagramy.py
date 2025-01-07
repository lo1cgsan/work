def popraw_dane(tekst):
    return tekst.strip().lower().replace(' ', '')

def sumuj_ASCII(tekst):
    suma = 0
    for znak in tekst:
        kod = ord(znak)
        suma = suma + kod
    return suma

w1 = input('Podaj wyraz: ')
w2 = input('Podaj wyraz: ')

# poprawność danych
w1 = popraw_dane(w1)
w2 = popraw_dane(w2)

print(w1, w2)
if sumuj_ASCII(w1) == sumuj_ASCII(w2):
    print('To anagramy.')
else:
    print('To nie anagramy.')
