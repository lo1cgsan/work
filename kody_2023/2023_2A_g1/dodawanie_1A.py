a = float(input("Podaj liczbę a: "))
b = float(input("Podaj liczbę b: "))
print("Podałeś:", a, b)
print("Suma:", a + b)
print("Różnica:", a - b)
print("Iloczyn:", a * b)

if b != 0:
    print("Iloraz:", a / b)
else:
    print("Błąd dzielenia przez zero!")
