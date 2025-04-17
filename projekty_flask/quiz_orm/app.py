import os
from flask import Flask, render_template, current_app
from db import db
import users, quiz

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    DATABASE=os.path.join(app.root_path, 'quiz.db'),
    SQLALCHEMY_DATABASE_URI='sqlite:///' +
                            os.path.join(app.root_path, 'quiz.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SITE_NAME='Quiz ORM SQLAlchemy'
))

db.init_app(app)

# rejestracja blueprintów
app.register_blueprint(users.bp)
app.register_blueprint(quiz.bp)

@app.route('/')
def index():
    # return 'Cześć, tu Python i Flask!'
    return render_template('index.html')

with app.app_context():
    if not os.path.exists(current_app.config['DATABASE']):
        import models
        from dane import pobierz_dane, dodaj_pytania
        db.create_all()
        pytania = pobierz_dane('pytania.csv')
        dodaj_pytania(pytania)

if __name__ == "__main__":
    app.run(debug=True)
