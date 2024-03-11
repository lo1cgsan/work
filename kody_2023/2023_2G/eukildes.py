def euklides1(a, b):
    licznik = 0

    while a != b:
        licznik += 1
        if a > b:
            a = a - b
        else:
            b = b - a

    print(a)
    print("Powtórzeń:", licznik)


def euklides2(a, b):
    licznik = 0
    if a < b:
        a, b = b, a
    while a > 0:
        licznik += 1
        a = a % b
        b = b - a
    
    print(b)
    print("Powtórzeń:", licznik)    


a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
euklides1(a, b)
euklides2(a, b)
