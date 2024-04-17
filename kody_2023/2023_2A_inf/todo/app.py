# todo/todo.py

from flask import Flask, g
from flask import render_template
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


@app.route('/zadania')
def zadania():
    db = get_db()
    kursor = db.execute('SELECT * FROM zadania')
    zadania = kursor.fetchall()
    return render_template('zadania_lista.html', zadania=zadania)


if __name__ == '__main__':
    app.run(debug=True)
