a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
c = int(input('Podaj c: '))


if a <= b:
    if c <= a:
        print("c, a, b")
    elif b <= c:
        print("a, b, c")
    else:
        print("a, c, b")
elif c <= b:
    print("c, b, a")
elif c <= a:
    print("b, c, a")
else:
    print("b, a, c")
