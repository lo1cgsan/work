from random import randint

def sort_wybor(lista):
    for i in range(1, len(lista)):
        element = lista[i]
        j = i - 1
        while j > - 1 and element < lista[j]:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = element

# lista = input("Podaj napis: ").lower()
# lista = list(lista)
#lista = []
#for i in range(10):
#    lista.append(randint(97, 122))
lista = [randint(97, 122) for i in range(10)]
print(lista)
sort_wybor(lista)
#for kod in lista:
#    print(chr(kod), end="")
print([chr(kod) for kod in lista])

napis = "abcxyz"
print([ord(el) for el in napis])
