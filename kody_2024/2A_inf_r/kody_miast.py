# kody_miast.py

miasta = ['Kielce', 'Gdynia', 'Wrocław']

for miasto in miasta:
    kod = miasto[0].lower() + '_' + miasto[1] + '_' + miasto[2]
    print(kod)

dni = ['pOniedziałek', 'WTorek', 'Środa']

for dzien in dni:
    kod = (dzien[0] + '-' + dzien[1]).lower()
    print(kod)
