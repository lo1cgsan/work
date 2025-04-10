from flask import (
    Blueprint, flash, g, render_template, request, redirect, url_for
)
from db import db
from models import Pytanie, Odpowiedz

bp = Blueprint('quiz', __name__, template_folder='quiz', url_prefix='/quiz')

@bp.route('/')
def index():
    pytania = db.session.execute(db.select(Pytanie)).scalars()
    return render_template('quiz/index.html', pytania=pytania)
