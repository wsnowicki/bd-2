from flask import Flask, render_template, request, redirect, url_for, session, jsonify, abort
from dotenv import load_dotenv
from os import getenv
import psycopg2
from login import *

# Wczytanie zmiennych z pliku .env
load_dotenv()
http_host = getenv("HTTP_HOST")
http_port = getenv("HTTP_PORT")
http_threads = getenv("HTTP_THREADS")


# Stworzenie aplikacji i nadanie tajnego klucza
app = Flask(__name__)
app.secret_key = getenv("HTTP_SECRET_KEY")


@app.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('search'))
    
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user'):
        return redirect(url_for('search'))
    
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        if (login_status := login_user(conn, login, password)) == Status.OK:
            session['user'] = login
            return redirect(url_for('search'))
        elif login_status == Status.WRONG_LOGIN:
            return render_template('login.html', alert="Błędny login lub hasło")
        elif login_status == Status.PASSWORD_TOO_LONG:
            return render_template('login.html', alert="Hasło jest za długie")
    return render_template('EkranLogowania.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('user'):
        return redirect(url_for('rejestracja'))

    # Jeszcze not implemented, brak htmla
    abort(501)


    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        email = request.form['email']
        tel = request.form['tel']
        if (register_status := register_user(conn, login, password,email,tel)) == Status.OK:
            session['user'] = login
            return redirect(url_for('search'))
        elif register_status == Status.USER_EXISTS:
            return render_template('rejestracja.html', alert="Użytkownik już istnieje")
        elif register_status == Status.PASSWORD_TOO_LONG:
            return render_template('rejestracja.html', alert="Hasło jest za długie")
    return render_template('rejestracja.html')


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
        db_user = getenv("DB_USER")
        db_password = getenv("DB_PASSWORD")
        db_host = getenv("DB_HOST", "127.0.0.1")
        db_port = getenv("DB_PORT", "5432")
        db_name = getenv("DB_DATABASE", "biblioteka")
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        cursor = connection.cursor()
        zap="SELECT books.title,books.is_available,books.year_published,books.isbn,books.cover_image,authors.name FROM books INNER JOIN authors ON books.author_id = authors.author_id WHERE authors.name LIKE '%"
        if '"' in str(author):
            pass
        elif "'" in str(author):
            pass
        else:
            zap+=str(author)
        zap+="%' AND books.title LIKE '%"
        if '"' in str(nazwa):
            pass
        elif "'" in str(author):
            pass
        else:       
            zap+=str(nazwa)
        zap+="%';"
        odp=cursor.execute(zap)
        if odp is not None:
            total_pagess = len(odp)//10 + bool(len(odp) % 10)
        else:
            total_pagess = 0
        return render_template('listaszukanych.html', books=odp, total_pages=total_pagess)
    return render_template('EkranWyszukiwania.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(501)
def not_implemented(e):
    return render_template('501.html'), 501

@app.route('/error')
def error():
    abort(404)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile')
def profile():
    abort(404)

if __name__ == '__main__':
    app.run(debug=True, host=http_host, port=http_port)

