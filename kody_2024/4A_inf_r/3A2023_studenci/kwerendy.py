import sqlite3

def wykonaj_zapytanie(kursor, zapytanie):
    kursor.execute(zapytanie)
    for rekord in kursor.fetchall():
        print(*rekord)


baza = 'studenci.db'
pol = sqlite3.connect(baza)
kursor = pol.cursor()

kwerenda = "SELECT sql FROM sqlite_master"
kwerenda = "SELECT imie, nazwisko FROM studenci"
kwerenda = "SELECT imie, nazwisko FROM studenci WHERE nazwisko = 'Krawiec'"
kwerenda = "SELECT imie, nazwisko FROM studenci WHERE nazwisko LIKE 'K%' "
kwerenda = "SELECT kod FROM miasta WHERE kod LIKE '53-_0_'"
kwerenda = "SELECT imie, nazwisko, nazwa FROM studenci INNER JOIN miasta ON studenci.id_miasta = miasta.id_miasta"
kwerenda = "SELECT imie, nazwisko, nazwa FROM studenci INNER JOIN uczelnie ON studenci.id_uczelni = uczelnie.id_uczelni"
kwerenda = """
    SELECT imie, nazwisko, u.nazwa, m.nazwa
    FROM studenci s
    INNER JOIN uczelnie u ON s.id_uczelni = u.id_uczelni
    INNER JOIN miasta m ON s.id_miasta = m.id_miasta
    """
# imie, nazwisko, miasto studentów 1 roku Uniwersytetu Królewskiego
kwerenda = """
    SELECT imie, nazwisko, m.nazwa
    FROM studenci s
    INNER JOIN uczelnie u ON s.id_uczelni = u.id_uczelni
    INNER JOIN miasta m ON s.id_miasta = m.id_miasta
    WHERE rok_studiow = 'I' AND u.nazwa = 'Uniwersytet Królewski'
    """

wykonaj_zapytanie(kursor, kwerenda)