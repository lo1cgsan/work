"""
Napisz program, który pobiera długość 3 odcinków
i sprawdza, czy da się z nich zbudować trójkąt.
"""
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

if a + b > c and b + c > a and a + c > b:
    print('Da się')
else:
    print('Nie da się')

if a + b <= c or b + c <= a or a + c <= b:
    print('Nie da się')
else:
    print('Da się')

# if a + b > c:
    # if b + c > a:
        # if a + c > b:
            # print('Da się')
        # else:
            # print('Nie da się')
    # else:
        # print('Nie da się')
# else:
    # print('Nie da się')

#jeżeli suma dwóch dowolnych boków > od trzeciego, to
#    print('Da się')
#w przeciwnym razie
#    print('Nie da się')
