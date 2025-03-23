import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort
from werkzeug.security import check_password_hash, generate_password_hash

from db import get_db

bp = Blueprint('users', __name__, template_folder='templates', url_prefix='/users')

@bp.route('/loguj', methods=['GET', 'POST'])
def loguj():
    if request.method == 'POST':
        login = request.form['login'].strip()
        haslo = request.form['haslo'].strip()

        db = get_db()
        error = None

        user = db.execute('SELECT * FROM user WHERE login = ?', [login]).fetchone()

        if user is None:
            error = 'Błędny login.'
        elif not check_password_hash(user['haslo'], haslo):
            error = 'Błędne hasło.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            flash(f'Zalogowano użytkownika {user['login']}!')
            return redirect(url_for('index'))
        flash(error)
    return render_template('users/loguj.html')

@bp.route('/dodaj', methods=['GET', 'POST'])
def dodaj():
    if request.method == 'POST':
        login = request.form['login'].strip()
        haslo = request.form['haslo'].strip()
        db = get_db()
        try:
            db.execute('INSERT INTO user VALUES (?, ?, ?)',
                       [None, login, generate_password_hash(haslo)])
            db.commit()
        except db.IntegrityError:
            flash(f'Podany login {login} jest już używany.')
        else:
            flash(f'Dodano konto {login}')
            return redirect(url_for('users.lista'))

    return render_template('users/dodaj.html')

@bp.before_app_request
def load_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute('SELECT * FROM user WHERE id = ?', [user_id]).fetchone()

@bp.route('/wyloguj')
def wyloguj():
    flash(f'Wylogowano użytkownika {g.user['login']}.')
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('users.loguj'))
        return view(**kwargs)
    return wrapped_view

def get_user(user_id):
    db = get_db()
    user = db.execute('SELECT * FROM user WHERE id = ?', [user_id]).fetchone()
    if user is None:
        abort(404, f'Użytkownik o id {user_id} nie istnieje.')
    return user

@bp.route('/<int:user_id>/usun', methods=['GET', 'POST'])
@login_required
def usun(user_id):
    user = get_user(user_id)
    if request.method == 'POST':
        db = get_db()
        db.execute('DELETE FROM user WHERE id = ?', [user_id])
        db.commit()
        flash(f'Usunięto użytkownika {user['login']}!')
        return redirect(url_for('index'))
    return render_template('users/usun.html', dane=user)
