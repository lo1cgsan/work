from flask import Flask, render_template

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pytania')
def pytania():

    return render_template('pytania.html', pytania=dane)

with app.app_context():
    if __name__ == "__main__":
        app.run(debug=True)

# flask --app app run --debug
