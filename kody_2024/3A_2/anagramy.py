# anagramy
w1 = input('Podaj wyraz: ')
w2 = input('Podaj wyraz: ')

w1 = w1.lower().replace(' ', '')
w2 = w2.lower().replace(' ', '')

def sumuj_ASCII(wyraz):
    suma = 0
    for znak in wyraz:
        kod = ord(znak)
        suma = suma + kod
    print(suma)
    return suma

toDo
