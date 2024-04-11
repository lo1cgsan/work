from random import randint

x = randint(1, 10)

for i in range(3):
    typ = int(input('Podaj typ: '))
    if typ == x:
        print('zgadłeś!')
print(x)
