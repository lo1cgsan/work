znak = input('Podaj znak: ')
n = int(input('Ile wierszy? '))

for i in range(n):
    for j in range(i+1):
        print(znak, end='')
    print()

for i in range(n):
    for j in range(n-i):
        print(znak, end='')
    print()
