a = int(input("Bok 1: "))
b = int(input("Bok 2: "))
c = int(input("Bok 3: "))

# warunki zagnieżdżone
# if a + b > c:
#    if a + c > b:
#        if b + c > a:
#            print("Da się!")
#            exit()

if a + b > c and a + c > b and b + c > a:
    print("Da się!")
else:
    print("Nie da się!")
