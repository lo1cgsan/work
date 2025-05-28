from flask import (
    Blueprint, flash, render_template, request, redirect, url_for
)
from db import query_db


bp = Blueprint('pytania', __name__, template_folder='pytania', url_prefix='/pytania')


@bp.route('/')
def lista():
    sql = 'SELECT pytanie.* FROM pytanie'
    pytania = query_db(sql)
    return render_template('pytania/pytanie_lista.html', pytania=pytania)


@bp.route('/dodaj', methods=['GET', 'POST'])
def dodaj():
    if request.method == 'POST':
        error = None
        print(request.form)
        pytanie = request.form['pytanie'].strip()
        if not pytanie:
            error = 'Nie wprowadzono pytania!'
        odpowiedzi = []
        l_poprawnych = 0
        for i in range(1, 4):
            poprawna = False
            if 'pop'+str(i+1) in request.form:
                poprawna = True
                l_poprawnych += 1
            odpowiedz = request.form['odp'+str(i+1)].strip()
            if not odpowiedz:
                error += f' Nie wprowadzono odpowiedzi {i+1}!'
                break
            odpowiedzi.append((odpowiedz, poprawna))
        if not l_poprawnych:
            error += ' Nie zaznaczono przynajmniej jednej poprawnej odpowiedzi!'

    return render_template('pytania/pytanie_dodaj.html')
# sql = 'SELECT p.*, o.* FROM pytanie p INNER JOIN odpowiedz o WHERE p.id=o.pytanie_id'
