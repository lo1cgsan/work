# dane wejściowe
a = int(input('Podaj bok a: '))
b = int(input('Podaj bok b: '))
c = int(input('Podaj bok c: '))

# sprawdzić warunki istnienia
# wypisać komunikat, czy da się zbudować trójkąt
# i – koniunkcja logiczna
if a + b > c and a + c > b and b + c > a:
    print('można zbudować')
else:
    print('nie można')

# lub – alternatywa logiczna
if a + b < c or a + c < b or b + c < a:
    print('nie można')
else:
    print('można zbudować')
