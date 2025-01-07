sekwencja = "abc"
#sekwencja = [1, 2, 3, 0]
#sekwencja = range(3)
#sekwencja = range(2, 11)
sekwencja = range(2, 11, 2)

suma = 0
for i in sekwencja:
    print(i)
    suma = suma + i

print(suma)
