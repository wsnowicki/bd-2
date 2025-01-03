from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'super_tajny_klucz_ktory_napewno_nie_jest_udostepniony_w_repo_w_plain_textZZ'

# Przykładowa baza użytkowników
users = {
    "admin": "admin",
    "user": "user"
}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        if login in users and users[login] == password:
            session['user'] = login
            return redirect(url_for('search'))
        else:
            return render_template('EkranLogowania.html', alert="Błędny login lub hasło")
    return render_template('EkranLogowania.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        nazwa_ksiazki = request.form.get('nazwaKsiazki', '')
        autor = request.form.get('autor', '')

        # Tutaj mock do wyszukiwania lol
        if nazwa_ksiazki == "Example" and autor == "Author":
            return jsonify({"result": "Znaleziono książkę"})
        else:
            return render_template('EkranWyszukiwania.html', alert="Brak wyników")
    return render_template('EkranWyszukiwania.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('Blad.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.201')

