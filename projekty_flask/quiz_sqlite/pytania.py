from flask import (
    Blueprint, render_template, request, redirect, url_for, flash, abort
)
from db import query_db, get_db

bp = Blueprint('pytania', __name__, template_folder='pytania', url_prefix='/pytania')

@bp.route('/')
def lista():
    sql = 'SELECT * FROM pytanie'
    pytania = query_db(sql)
    return render_template('pytania/pytanie_lista.html', pytania=pytania)

@bp.route('/dodaj', methods=['GET', 'POST'])
def dodaj():

    if request.method == 'POST':
        pytanie = request.form['pytanie'].strip()
        if pytanie:
            db = get_db()
            sql = 'INSERT INTO pytanie VALUES (?, ?)'
            db.execute(sql, [None, pytanie])
            db.commit()
            flash(f'Dodano pytanie: {pytanie}')
            return redirect(url_for('pytania.lista'))
        else:
            flash('Nie podałeś pytania!')

    return render_template('pytania/pytanie_dodaj.html')

def get_pytanie(id):
    sql = 'SELECT * FROM pytanie WHERE id = ?'
    pytanie = query_db(sql, [id], one=True)
    if pytanie:
        return pytanie
    else:
        abort(404)

@bp.route('/odpowiedzi/<int:pid>', methods=['GET', 'POST'])
def dodaj_odpowiedzi(pid):
    pytanie = get_pytanie(int(pid))
    print(pytanie)
    if request.method == 'POST':
        print(request.form)

    return render_template('pytania/odpowiedzi_dodaj.html', pytanie=pytanie)
