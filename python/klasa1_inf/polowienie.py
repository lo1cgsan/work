def minimum(lista):
    licznik = 0
    min_w = lista[0]
    for i in range(1, len(lista)):
        licznik += 1
        if lista[i] < min_w:
            min_w = lista[i]
    print("Powtórzenia min:", licznik)
    return min_w
    
def maksimum(lista):
    licznik = 0
    max_w = lista[0]
    for i in range(1, len(lista)):
        licznik += 1
        if lista[i] > max_w:
            max_w = lista[i]    
    print("Powtórzenia max:", licznik)
    return max_w

lista = [3, 2, 5, 8, 10, 1, 6, 7, 4]
toDo: 
#minimum(lista)
#maksimum(lista)
#exit()

l_min = []
l_max = []
licznik = 0
for i in range(0, len(lista), 2):
    licznik += 1
    if lista[i] > lista[i+1]:
        l_max.append(lista[i])
        l_min.append(lista[i+1])
    else:
        l_min.append(lista[i])
        l_max.append(lista[i+1])
print("Powtórzenia poł.:", licznik)

print(l_min)
print(l_max)
print(minimum(l_min))
print(maksimum(l_max))
