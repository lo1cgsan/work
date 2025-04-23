# policz średnią pobranych ocen

oceny_przedmioty = {}  # słownik ocen

przedmiot = input('Podaj przedmiot: ')
ile_ocen = int(input('Ile ocen: '))

oceny = []
for i in range(ile_ocen):
    oceny.append(int(input('Podaj ocenę: ')))

oceny_przedmiot[przedmiot] = oceny

oceny_przedmioty = {
    'polski' = [4, 2, 6, 5],
    'angielski' = [1, 2, 6, 7],
    'matematyka' = {5:0.1, 6:0.3}
}
