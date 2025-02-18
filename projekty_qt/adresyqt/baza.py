from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtWidgets import QMessageBox

def wyswietl_komunikat(t, k, r=''):

    if r == '':
        QMessageBox.information(None, t, k)
    elif r == 'warn':
        QMessageBox.warning(None, t, k, QMessageBox.Cancel)
    elif r == 'crit':
        QMessageBox.critical(None, t, k, QMessageBox.Cancel)
    elif r == 'ask':
        odp = QMessageBox.question(None, t, k, QMessageBox.Yes | QMessageBox.No)
        return odp

def polacz():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("adresy.db")
    if not db.open():
        wyswietl_komunikat("Błąd połączenia z bazą",
                           "Nie można połączyć się z bazą\n Kliknij Anuluj")
    db.exec("""CREATE TABLE IF NOT EXISTS adresy(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nazwa TEXT,
                adres TEXT
            )""")

    if db.lastError().isValid():
        wyswietl_komunikat("Błąd bazy", "Nie można utworzyć tabeli")
        return False

    return True

def czytaj_dane():
    kontakty = []
    q = QSqlQuery()
    odp = q.exec("SELECT * FROM adresy ORDER BY id")
    if not odp:
        wyswietl_komunikat("Błąd bazy", "Nie można odczytać danych")
    else:
        while q.next():
            kontakty.append({q.value('nazwa'): q.value('adres')})

    return kontakty

def wykonaj_zapytanie(query, data):
    q = QSqlQuery()
    q.prepare(query)
    for d in data:
        q.addBindValue(d)
    wynik = q.exec()
    if not wynik:
        wyswietl_komunikat('Błąd bazy', 'Błąd zapisu!')
        return False

    return True