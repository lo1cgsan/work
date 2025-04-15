from flask import Flask, request
from flask import render_template

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='bardzosekretnymkluczem',
    SITE_NAME='Quiz Python',
))

dane = [
    {'pytanie': 'Stolica Hiszpanii to:',
     'odpowiedzi': ['Madryt', 'Warszawa', 'Barcelona'],
     'odpok': 'Madryt'}
]

@app.route('/pytania', methods=['GET', 'POST'])
def pytania():
    if request.method == 'POST':
        odpowiedzi = request.form
        print(request.form)


    return render_template('pytania.html', pytania=dane)

# widok, view
@app.route('/')
def index():
    # return 'Cześć, tu Python i Flask'
    return render_template('index.html')

with app.app_context():
    if __name__ == "__main__":
        app.run(debug=True)
