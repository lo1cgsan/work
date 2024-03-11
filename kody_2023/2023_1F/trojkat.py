"""
jeżeli suma dwóch dowolnych boków > od trzeciego
    wypisz 'Da się zbudować'
w przeciwnym razie
    wypisz 'Nie da się!'
"""

# dane wejściowe
a = int(input("Podaj bok a: "))
b = int(input("Podaj bok b: "))
c = int(input("Podaj bok c: "))

# przykład zagnieżdżonych intsrukcji warunkowych

# if a + b > c:
#    if a + c > b:
#        if b + c > a:
#            print("Da się zbudować")
#            exit()

if a + b > c and a + c > b and b + c > a:
    print("Da się zbudować")
else:
    print("Nie da się")

if a + b <= c or a + c <= b or b + c <= a:
    print("Nie da się")
else:
    print("Da się zbudować")
