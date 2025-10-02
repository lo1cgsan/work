plik_danych = 'dane2.txt'

with open(plik_danych) as plik:
    for wiersz in plik:
        dane = wiersz.strip().split('\t')
        print(dane)
        print(f'Liczba nieobecności: {len(dane)}')


with open(plik_danych) as plik:
    for wiersz in plik:
        tydzien = wiersz.replace('\n', '')
        tydzien = tydzien.split('\t')
        # for dzien in tydzien:
        obecnosci = [0, 0, 0, 0, 0]
        nieobecnosci = [0, 0, 0, 0, 0]
        for i in range(len(tydzien)):
            dzien = tydzien[i]
            if dzien:
                print('nieobecny')
                nieobecnosci[i] += 1
            else:
                obecnosci[i] += 1
    print('Obecności:', obecnosci)
