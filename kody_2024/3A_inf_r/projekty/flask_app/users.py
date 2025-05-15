from flask import Blueprint, render_template

bp = Blueprint('users', __name__, template_folder='templates', url_prefix='/users')

@bp.route('/loguj', methods=['GET', 'POST'])
def loguj():
    return render_template('users/user_loguj.html')