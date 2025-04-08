import os
from flask import Flask, render_template, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    DATABASE=os.path.join(app.root_path, 'quiz.db'),
    SQLALCHEMY_DATABASE_URI='sqlite:///' +
                            os.path.join(app.root_path, 'quiz.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    TYTUL='Quiz ORM SQLAlchemy'
))

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

@app.route('/')
def index():
    return 'Cześć, tu Python i Flask!'

with app.app_context():
    if not os.path.exists(current_app.config['DATABASE']):
        db.create_all()
    if __name__ == "__main__":
        app.run(debug=True)
