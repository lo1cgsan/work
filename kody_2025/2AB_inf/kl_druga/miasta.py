plik_danych = 'miasta.txt'

with open(plik_danych) as plik:
    for wiersz in plik:
        miasto = wiersz.strip()
        if miasto:
            print(miasto[0].lower() + "_" + miasto[1] + "_" + miasto[2])
            print("_".join(miasto[0:3]).lower())
