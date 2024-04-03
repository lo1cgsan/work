"""
Napisz program, który pobiera tyle ocen, ile chce podać użytkownik,
liczy i wpypisuje ich srednią.
"""
ile_ocen = int(input("Ile ocen? "))
suma = 0

for i in range(ile_ocen):
    print(i)
    o1 = int(input("Podaj ocena: "))
    if o1 > 0 and o1 < 7:
        suma = suma + o1
    else:
        ile_ocen = ile_ocen - 1

srednia = suma / ile_ocen

print(srednia)

