from baza import Baza
from dataclasses import dataclass

plik_sql = 'slownik.sql'
plik_bazy = 'slownik.db'

@dataclass
class Wyraz():
    wyraz: str
    znaczenia: list
    id: int = -1

# slownik = {
#     'go': obiekt wyraz
#     'watch': obiekt wyraz
# }


class Slownik(Baza):
    def __init__(self, nazwa, plik_bazy, plik_sql):
        super().__init__(plik_bazy, plik_sql)
        self.nazwa = nazwa
        self.slownik = {}
        # self.slownik = {'go': Wyraz('go', ['iść', 'biec'])}
        self.wczytaj_dane()
        self.wybierz_operacje()

    def wybierz_operacje(self):
        menu = """
        1) Dodaj wyraz
        2) Edytuj wyraz
        3) Usuń wyraz
        4) Wypisz wyrazy
        5) Zapisz wyraz
        0) Zamknij
        """
        odp = True
        while odp:
            print(menu)
            odp = int(input('Wybierz operację: ').strip())
            if odp == 1:
                self.dodaj_wyraz()
            elif odp == 2:
                self.edytuj_wyraz()
            elif odp == 3:
                self.usun_wyraz()
            elif odp == 4:
                self.wypisz_wyrazy()
            elif odp == 5:
                self.zapisz_dane()

    def wczytaj_dane(self):
        zapytanie = """
            SELECT w.*, znaczenie FROM wyrazy w
            INNER JOIN wyraz_znaczenie wz ON w.id_wyraz = wz.id_wyraz
            INNER JOIN znaczenia z ON z.id_znaczenie = wz.id_znaczenie 
        """
        wynik = self.wykonaj_select(zapytanie)
        if wynik:
            for rek in wynik:
                id, wyraz, znaczenie = rek[0], rek[1], rek[2]
                if wyraz not in self.slownik:
                    self.slownik[wyraz] = Wyraz(wyraz, [znaczenie], id)
                else:
                    self.slownik[wyraz].znaczenia.append(znaczenie)

    def dodaj_wyraz(self):
        wyraz = input('Podaj wyraz: ').strip()
        if wyraz in self.slownik.keys():
            print('Słowo jest już w bazie.')
        else:
            self.slownik[wyraz] = Wyraz(wyraz=wyraz, znaczenia=self.pobierz_znaczenia())

    def pobierz_znaczenia(self):
        znaczenia = input('Podaj znaczenie(a) oddzielone przecinkami:\n')
        znaczenia = znaczenia.split(',')
        znaczenia = [z.strip() for z in znaczenia]  # wyrażenie listowe
        return znaczenia

    def edytuj_wyraz(self):
        wyraz = self.wypisz_wyrazy(True)
        print(wyraz)

    def usun_wyraz(self):
        wyraz = self.wypisz_wyrazy(True)
        if wyraz.isdigit():
            zapytanie = 'DELETE FROM wyrazy WHERE id_wyraz = ?'
            self.wykonaj_zapytanie(zapytanie, (wyraz,))
            w = self.get_wyraz(wyraz)
            print('Usuwam wyraz:', w)
            del self.slownik[w]
            zapytanie = 'SELECT id_znaczenie FROM wyraz_znaczenie WHERE id_wyraz = ?'
            wyniki = self.wykonaj_select(zapytanie, (wyraz,))
            zapytanie = 'DELETE FROM znaczenia WHERE id_znaczenie = ?'
            for z in wyniki:
                self.wykonaj_zapytanie(zapytanie, z)
        else:
            del self.slownik[wyraz]

    def zapisz_dane(self):
        for w, w_obj in self.slownik.items():
            if w_obj.id == -1:
                zapytanie = 'INSERT INTO wyrazy(wyraz) VALUES(?)'
                id_wyraz = self.wykonaj_insert(zapytanie, (w,))
                id_znaczen = []
                for z in w_obj.znaczenia:
                    zapytanie = 'INSERT INTO znaczenia(znaczenie) VALUES(?)'
                    id_z = self.wykonaj_insert(zapytanie, (z,))
                    id_znaczen.append(id_z)

                dane = zip([id_wyraz] * len(id_znaczen), id_znaczen)
                zapytanie = 'INSERT INTO wyraz_znaczenie(id_wyraz, id_znaczenie) VALUES(?, ?)'
                self.wykonaj_insert_many(zapytanie, dane)
            else:
                wyraz = self.wykonaj_select('SELECT wyraz FROM wyrazy WHERE id_wyraz = ?', (w_obj.id,))
                print(wyraz)
                if w != wyraz:
                    self.wykonaj_zapytanie('UPDATE wyrazy SET wyraz = ? WHERE id_wyraz = ?', (w, w_obj.id))
                znaczenia = self.wykonaj_select("""
                    SELECT wyraz, znaczenie
                    FROM wyraz_znaczenie wz, wyrazy w, znaczenia z
                    WHERE wz.id_wyraz = w.id_wyraz
                    AND wz.id_znaczenie = z.id_znaczenie
                    AND w.id_wyraz = ?
                """, (w_obj.id,))
                print(znaczenia)

    def wypisz_wyrazy(self, wybor=False):
        if self.slownik:
            for w in self.slownik.values():
                print(w)
            if wybor:
                odp = input('Podaj wyraz lub identyfikator wyrazu: ')
                return odp
        else:
            print('Brak danych!')

    def get_wyraz(self, atrybut):
        wynik = None
        for w in self.slownik.values():
            if atrybut.isdigit() and (w.id == int(atrybut)):
                wynik = w.wyraz
        return wynik

slownik = Slownik('angielski', plik_bazy, plik_sql)