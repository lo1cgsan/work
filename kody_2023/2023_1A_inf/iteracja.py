#for x in "abc":
#    print(x)

#for x in (1, "a", 3, "b", 5):
#    print(x)

#for x in range(10):
#    print(x, end=" ")

# wypisz liczby od 1 do 1000
# for x in range(1, 1001):
    print(x, end=" ")
    
# zsumuj liczby od 1 do 100
#suma = 0
#for x in range(1, 101):
#    suma = suma + x  # powiększ suma o x
#    print(suma)

# zsumuj liczby parzyste od 0 do 100
#suma = 0
#for x in range(101):
#    if x % 2 == 0:
#        print(x)
#        suma += x  # powiększ suma o x

suma = 0        
for x in range(0, 51):
    suma += 2 * x
print(suma)

suma = 0
for x in range(0, 101, 2):
    suma += x
print(suma)

