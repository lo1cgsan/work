# dane wejściowe
a = int(input('Podaj bok a: '))
b = int(input('Podaj bok b: '))
c = int(input('Podaj bok c: '))

# sprawdzić warunki istnienia
# wypisać komunikat, czy da się zbudować trójkąt
# i – koniunkcja logiczna
if a + b > c:
    if a + c > b:
        if b + c > a:
            print('można zbudować')
        else:
            print('nie można')
    else:
        print('nie można')
else:
    print('nie można')
