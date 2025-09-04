# Program pobiera n liczb i:
# sumuje liczby całkowite dodatnie
# sumuje liczby parzyste

# pobierz liczbę całkowitą n
n = int(input('Ile liczb podasz? '))

suma = 0
suma_parzyste = 0
for i in range(n):
    # pobierz liczbę całkowitą a
    a = int(input('Podaj liczbę? '))
    if a > 0:
        suma = suma + a
        if a % 2 == 0:
            suma_parzyste += a


print('Suma liczb dodatnich:', suma)
