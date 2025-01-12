from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from dotenv import load_dotenv
from os import getenv

# Wczytanie zmiennych z pliku .env
load_dotenv()
http_host = getenv("HTTP_HOST")
http_port = getenv("HTTP_PORT")
http_threads = getenv("HTTP_THREADS")

# Stworzenie aplikacji i nadanie tajnego klucza
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
        nazwa = request.form['nazwa']
        author = request.form['autor']
        nazwa_ksiazki = request.form.get('nazwaKsiazki', '')
        autor = request.form.get('autor', '')

        # Tutaj wyszukiwanie
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST", "127.0.0.1")
        db_port = os.getenv("DB_PORT", "5432")
        db_name = os.getenv("DB_DATABASE", "biblioteka")
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        cursor = connection.cursor()
        zap="SELECT books.title,books.is_available,books.year_published,books.isbn,authors.name FROM books INNER JOIN authors ON books.author_id = authors.author_id WHERE authors.name LIKE "
        if '"' in str(author):
            pass
        elif "'" in str(author):
            pass
        else:
            zap+=str(author)
        zap+="% AND books.title LIKE "
        if '"' in str(nazwa):
            pass
        elif "'" in str(author):
            pass
        else:       
            zap+=str(nazwa)
        zap+="%;"
        odp=cursor.execute(zap)
        return jsonify(odp)
    return render_template('EkranWyszukiwania.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('Blad.html'), 404

@app.route('/error')
def error():
    return 404


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile')
def profile():
    return 404

if __name__ == '__main__':
    app.run(debug=True, host=http_host, port=http_port)

