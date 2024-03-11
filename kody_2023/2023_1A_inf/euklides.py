def euklides1():

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(a)


a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
