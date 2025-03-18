def nwd1(a, b):
    while a != b:
        print(a, b)
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def nwd2(a, b):
    while a > 0:
        a = a % b
    toDo

a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
nwd = nwd1(a, b)
print(nwd)
