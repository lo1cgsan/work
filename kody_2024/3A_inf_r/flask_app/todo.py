from flask import Blueprint, render_template, request, session, flash, redirect, url_for, g
from werkzeug.security import check_password_hash, generate_password_hash
from db import query_db, get_db
from users import login_required

bp = Blueprint('todo', __name__, template_folder='templates', url_prefix='/todo')

@bp.route('/')
def index():
    sql = 'SELECT * FROM zadanie WHERE user_id=? ORDER BY data_dodania DESC'
    zadania = query_db(sql, [g.user['id']])
    return render_template('todo/lista_zadan.html', zadania=zadania)


@bp.route('/dodaj', methods=['GET', 'POST'])
# @login_required
def dodaj():
    if request.method == 'POST':
        zadanie = request.form['zadanie'].strip()
        db = get_db()
        try:
            db.execute('INSERT INTO zadanie (user_id, zadanie) VALUES (?, ?)',
                       [g.user['id'], zadanie])
            db.commit()
        except db.IntegrityError:
            flash(f'Błędne dane!')
        else:
            flash(f'Dodano zadanie {zadanie}')
            return redirect(url_for('todo.index'))

    return render_template('todo/zadanie_dodaj.html', akcja='Zapisz')
