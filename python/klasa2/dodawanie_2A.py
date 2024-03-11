a = input("Podaj liczbę a: ")
b = input("Podaj liczbę b: ")
print("Suma:", float(a) + float(b))
print("Różnica:", float(a) - float(b))
print("Iloczyn:", float(a) * float(b))

if float(b) != 0:
    print("Iloraz:", float(a) / float(b))
else:
    print("Nie dziel przez zero!")
