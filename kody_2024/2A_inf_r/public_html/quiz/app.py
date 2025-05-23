from flask import Flask, render_template, request, redirect, flash, url_for

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

@app.route('/pytania', methods=['GET', 'POST'])
def pytania():
    if request.method == 'POST':
        print(request.form)
        punkty = 0
        odpowiedzi = request.form
        for p_nr, odp in odpowiedzi.items():
            if odp == dane[int(p_nr)]['odpok']:
                punkty += 1

        flash(f'Liczba poprawnych odpowiedzi: {punkty}')
        return redirect(url_for('index'))

    return render_template('pytania.html', pytania=dane)

with app.app_context():
    if __name__ == "__main__":
        app.run(debug=True)

# flask --app app run --debug
