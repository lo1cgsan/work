"""
Napisz program, który sprawdza, czy z 3 podanych boków
a, b, c da się zbudować trójkąt.
"""
a = int(input("Podaj bok: "))
b = int(input("Podaj bok: "))
c = int(input("Podaj bok: "))

if a + b > c and a + c > b and b + c > a:
    print("Da się")
else:
    print("Nie da się")
#if a + b > c:
#    if a + c > b:
#        if b + c > a:
#            print("Da się")
#            exit() # zakończ program
#        else:
#            print("Nie da się")
#    else:
#        print("Nie da się")
#else:
#    print("Nie da się")
