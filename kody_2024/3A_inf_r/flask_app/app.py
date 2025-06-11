import os
from flask import Flask, request, flash, redirect, url_for, current_app
from flask import render_template
from db import init_app, init_db
import users, todo, czat

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='bardzosekretnymkluczem',
    SITE_NAME='Aplikacja Flask',
    DATABASE=os.path.join(app.root_path, 'db.sqlite')
))

init_app(app)
app.register_blueprint(users.bp)
app.register_blueprint(todo.bp)
app.register_blueprint(czat.bp)

dane = [
    {'pytanie': 'Stolica Hiszpanii to:',
     'odpowiedzi': ['Madryt', 'Warszawa', 'Barcelona'],
     'odpok': 'Madryt'}
]

@app.route('/pytania', methods=['GET', 'POST'])
def pytania():
    if request.method == 'POST':
        odpowiedzi = request.form
        punkty = 0
        for pnr, odp in odpowiedzi.items():
            if odp == dane[int(pnr)]['odpok']:
                punkty += 1
        flash(f'Liczba poprawnych odpowiedzi: {punkty}')
        return redirect(url_for('pytania'))

    return render_template('pytania.html', pytania=dane)

# widok, view
@app.route('/')
def index():
    # return 'Cześć, tu Python i Flask'
    return render_template('index_.html')

with app.app_context():
    if not os.path.exists(current_app.config['DATABASE']):
        init_db()
    if __name__ == "__main__":
        app.run(debug=True)

# flask --app app run --debug