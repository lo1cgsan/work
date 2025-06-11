from flask import (
    Blueprint, flash, render_template, request, redirect, url_for
)
from db import query_db, get_db


bp = Blueprint('pytania', __name__, template_folder='pytania', url_prefix='/pytania')


@bp.route('/')
def lista():
    sql = 'SELECT pytanie.* FROM pytanie'
    pytania = query_db(sql)
    return render_template('pytania/pytanie_lista.html', pytania=pytania)


@bp.route('/dodaj', methods=['GET', 'POST'])
def dodaj():
    pytanie_form = {'pytanie': '', 'odpowiedzi': [], 'poprawne': []}
    errors = []

    if request.method == 'POST':
        print(request.form)

        pytanie = request.form['pytanie'].strip()
        if not pytanie:
            errors.append = 'Nie wpisano pytania!'

        odpowiedzi = request.form.getlist('odpowiedzi')
        for i, o in enumerate(odpowiedzi):
            if not o.strip():
                errors.append(f' Nie wpisano odpowiedzi {i+1}!')
            else:
                odpowiedzi[i] = o.strip()

        poprawne = request.form.getlist('poprawne')
        if not len(poprawne):
            errors.append(' Nie zaznaczono przynajmniej jednej poprawnej odpowiedzi!')
        print(poprawne)
        if not errors:
            sql = 'INSERT INTO pytanie VALUES (?, ?)'
            db = get_db()
            cur = db.execute(sql, [None, pytanie])
            # db.commit()
            pytanie_id = cur.lastrowid
            sql = 'INSERT INTO odpowiedz VALUES (?, ?, ?, ?)'
            for i, odp in enumerate(odpowiedzi):
                poprawna = False
                if str(i+1) in poprawne:
                    poprawna = True
                print([None, pytanie_id, odp, poprawna])
                db.execute(sql, [None, pytanie_id, odp, poprawna])
            db.commit()
            flash(f'Dodano pytanie: {pytanie}')
            return redirect(url_for('pytania.lista'))

        # jeżeli formularz zawiera błędy
        pytanie_form['pytanie'] = pytanie
        pytanie_form['odpowiedzi'] = odpowiedzi

    return render_template('pytania/pytanie_dodaj.html', errors=errors, pytanie_form=pytanie_form, akcja='Dodaj')

# sql = 'SELECT p.*, o.* FROM pytanie p INNER JOIN odpowiedz o WHERE p.id=o.pytanie_id'
