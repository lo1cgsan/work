# prosty kalkulator
# dane wejściowe
# liczba rzeczywista x
# liczba rzeczywista y
# dzialanie
# +, -, *, /

x = float(input('Podaj liczbę x: '))
y = float(input('Podaj liczbę y: '))

wybor = input('Jakie działanie? ')

if wybor == '+':
    print(x + y)
elif wybor == '-':
    print(x - y)
elif wybor == '*':
    print(x * y)
elif wybor == '/':
    if y != 0:
        print(x / y)
    else:
        print('Błąd dzielenia przez zero!')

