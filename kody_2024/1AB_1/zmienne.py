a = float(input('Podaj liczbę: '))
b = float(input('Podaj liczbę: '))

suma = a + b
print('Suma =', suma)

roznica = a - b
iloczyn = a * b

if b != 0:
    iloraz1 = a / b   # dzielenie rzeczywiste
    iloraz2 = a // b  # dzielenie całkowite
    iloraz3 = a % b   # dzielenie z resztą (modulo)
else:
    print('nie można dzielić przez zero')

print('Różnica =', roznica)
print('Iloczyn =', iloczyn)
print('Dzielenie rzeczywiste =', iloraz1)
print('Dzielenie całkowite =', iloraz2)
print('Dzielenie modulo =', iloraz3)
