ile_ocen = 5
oceny = []  # pusta lista


for _ in range(ile_ocen):
    ocena = int(input('Podaj ocenę: '))
    oceny.append(ocena)

print(oceny)
print(sum(oceny) / len(oceny))
