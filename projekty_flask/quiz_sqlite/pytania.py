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

@bp.route('/edytuj/<int:pid>', methods=['GET', 'POST'])
def edytuj(pid):
    pytanie = get_pytanie(int(pid))
    if request.method == 'POST':
        pytanie_nowe = request.form['pytanie'].strip()
        if pytanie_nowe and pytanie_nowe != pytanie['pytanie']:
            db = get_db()
            sql = 'UPDATE pytanie SET pytanie = ? WHERE id = ?'
            db.execute(sql, [pytanie_nowe, pid])
            db.commit()
            flash(f'Zaktualizowano pytanie: {pytanie_nowe}')
            return redirect(url_for('pytania.lista'))
        else:
            flash('Nie podałeś lub nie zmieniłeś pytania!')
    return render_template('pytania/pytanie_dodaj.html', pytanie=pytanie)

@bp.route('/odpowiedzi/dodaj/<int:pid>', methods=['GET', 'POST'])
def odpowiedzi_dodaj(pid):
    pytanie = get_pytanie(int(pid))
    print(pytanie[0])
    if request.method == 'POST':
        odpowiedzi = request.form.getlist('odpowiedzi')
        poprawne = request.form.getlist('poprawne')
        print(odpowiedzi)
        print(poprawne)
        db = get_db()
        for i, odp in enumerate(odpowiedzi):
            poprawna = True if str(i+1) in poprawne else False
            sql = 'INSERT INTO odpowiedz VALUES (?, ?, ?, ?)'
            db.execute(sql, [None, pid, odp, poprawna])
        db.commit()
        flash(f'Dodano odpowiedzi do pytania: {pytanie.pytanie}')
        return redirect(url_for('pytania.lista'))

    return render_template('pytania/odpowiedzi_dodaj.html', pytanie=pytanie)

def get_odpowiedzi(pid):
    sql = 'SELECT * FROM odpowiedz WHERE pytanie_id = ?'
    odpowiedzi = query_db(sql, [pid])
    if odpowiedzi:
        return odpowiedzi
    else:
        abort(404)

@bp.route('/odpowiedzi/edytuj/<int:pid>', methods=['GET', 'POST'])
def odpowiedzi_edytuj(pid):
    pytanie = get_pytanie(int(pid))
    odpowiedzi = get_odpowiedzi(int(pid))
    print(odpowiedzi)

    return render_template('pytania/odpowiedzi_dodaj.html', pytanie=pytanie, odpowiedzi=odpowiedzi)