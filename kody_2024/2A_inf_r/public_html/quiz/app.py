from flask import (
    Flask, render_template, current_app
)
import os
from db import init_app, init_db
import pytania


app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    SITE_NAME='Pytania Flask',
    DATABASE=os.path.join(app.root_path, 'db.sqlite')
))

init_app(app)

# rejestracja blueprintów
app.register_blueprint(pytania.bp)


@app.route('/')
def index():
    return render_template('index.html')


with app.app_context():
    if not os.path.exists(current_app.config['DATABASE']):
        init_db()
    if __name__ == "__main__":
        app.run(debug=True)

# flask --app app run --debug
