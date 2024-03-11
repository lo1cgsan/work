""" trojkat_abc.py
    Program pobiera 3 boki trójkąta (liczby rzeczywiste)
    i sprawdza, czy da się z nich zbudować trójkąt.
    Program wypisuje komunikat: 'Da się' lub 'Nie da się'.
"""

a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
c = float(input("Podaj bok c: "))

if a + b > c:
    if a + c > b:
        if b + c > a:
            print("Da się!")
        else:
            print("Nie da się")
    else:
        print("Nie da się")
else:
    print("Nie da się")

if a + b > c and a + c > b and b + c > a:
    print("Da się!")
else:
    print("Nie da się")
