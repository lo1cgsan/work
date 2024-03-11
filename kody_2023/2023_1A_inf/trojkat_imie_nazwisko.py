# Napisz program, który pobiera trzy boki trójkąta
# i sprawdza, czy da się z nich zbudować trójkąt.

# Jeżeli trójkąt można zbudować, sprawdź czy jest to
# trókąt prostokątny.

# Dane: a, b, c – liczby całkowite dodatnie
# Wynik działania programu:
# wypisz odpowiedni komunikat: "da się zbudwoać" lub "nie da się zbudować"
# jeżeli da się, wypisz: "prostokątny" lub "nie prostokątny"

import math

a = 3
b = 4
c = 5

if a + b > c and a + c > b and b + c > a:
    print("da się")
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print("prostokątny")
    p = 0.5 * (a + b + c)
    pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("Pole:", pole)
else:
    print("nie da się")

