# todo/app.py

from flask import Flask, g
from flask import request, redirect, url_for, flash
from flask import render_template
from datetime import datetime
import os
import sqlite3

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    DATABASE=os.path.join(app.root_path, 'db.sqlite'),
    SITE_NAME='Moje zadania'
))


def get_db():
    """Funkcja tworząca połączenie z bazą danych"""
    if not g.get('db'):  # jeżeli brak połączenia, to je tworzymy
        con = sqlite3.connect(app.config['DATABASE'])
        con.row_factory = sqlite3.Row
        g.db = con  # zapisujemy połączenie w kontekście aplikacji
    return g.db  # zwracamy połączenie z bazą


@app.teardown_appcontext
def close_db(error):
    """Zamykanie połączenia z bazą"""
    if g.get('db'):
        g.db.close()


@app.route('/')
def index():
    # return '<h1>Cześć, tu Python!</h1>'
    return render_template('index.html')


@app.route('/zadania', methods=['GET', 'POST'])
def zadania():

    if request.method == 'POST':
        zadanie = request.form['zadanie'].strip()
        if zadanie:
            zrobione = 0
            data_pub = datetime.now()
            db = get_db()
            db.execute('INSERT INTO zadania VALUES (?, ?, ?, ?)',
                       [None, zadanie, zrobione, data_pub])
            db.commit()  # zatwierdzenie zmian w bazie danych
            flash('Dodano nowe zadanie.')
            return redirect(url_for('zadania'))

    db = get_db()
    kursor = db.execute('SELECT * FROM zadania')
    zadania = kursor.fetchall()
    return render_template('zadania_lista.html', zadania=zadania)


@app.route('/zrobione', methods=['POST'])
def zrobione():
    zadanie_id = request.form['id']
    db = get_db()
    db.execute('UPDATE zadania SET zrobione=1 WHERE id=?', [zadanie_id])
    db.commit()
    flash('Zmieniono status zadania.')
    return redirect(url_for('zadania'))

if __name__ == '__main__':
    app.run(debug=True)
