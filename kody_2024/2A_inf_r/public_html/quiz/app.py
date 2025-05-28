from flask import (
    Flask, render_template, request, redirect, flash, url_for, current_app
)
import os
from db import init_app, init_db
import pytania


app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    SITE_NAME='Quiz Flask',
    DATABASE=os.path.join(app.root_path, 'db.sqlite')
))

init_app(app)

# rejestracja blueprintów
app.register_blueprint(pytania.bp)


@app.route('/')
def index():
    return render_template('index.html')


dane = [
    {
        'pytanie': 'Stolica Hiszpanii to:',
        'odpowiedzi': ['Warszawa', 'Madryt', 'Barcelona'],
        'odpok': 'Madryt'
    },
    {
        'pytanie': 'Symbol pierwiastka Helu to:',
        'odpowiedzi': ['Fe', 'H', 'He'],
        'odpok': 'He'
    }
]

# @app.route('/pytania', methods=['GET', 'POST'])
# def pytania():
#     if request.method == 'POST':
#         print(request.form)
#         punkty = 0
#         odpowiedzi = request.form
#         for p_nr, odp in odpowiedzi.items():
#             if odp == dane[int(p_nr)]['odpok']:
#                 punkty += 1

#         flash(f'Liczba poprawnych odpowiedzi: {punkty}')
#         return redirect(url_for('pytania'))

#     return render_template('pytania.html', pytania=dane)

with app.app_context():
    if not os.path.exists(current_app.config['DATABASE']):
        init_db()
    if __name__ == "__main__":
        app.run(debug=True)

# flask --app app run --debug
