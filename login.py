"""
Moduł odpowiedzialny za przetwarzanie logowania użytkownika.

Funkcje zawarte w module są odpowiedzialne za przetwarzanie logowania użytkownika. Od szyfrowania haseł, po sprawdzanie poprawności danych logowania.




Functions:
    encrypt_password: Szyfruje hasło użytkownika.
    veryify_password: Sprawdza poprawność hasła użytkownika.

Usage:
    Zaimportuj moduł do swojego skryptu i wywołaj odpowiednią funkcję.
"""

import bcrypt
from dotenv import load_dotenv
from os import getenv
import psycopg2
users_db = {}
load_dotenv()
http_host = getenv("HTTP_HOST")
http_port = getenv("HTTP_PORT")
http_threads = getenv("HTTP_THREADS")
def encrypt_password(password):
    """Funkcja do szyfrowania hasła."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def verify_password(password, hashed):
    """Funkcja do weryfikacji hasła."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def register_user(username, password):
    email='testowy@gmail'
    telephone='111333222'
    """Funkcja rejestrująca użytkownika."""
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
    # Tutaj będzie zapytanie do bazy danych.
    cursor = connection.cursor()
    zap = "SELECT COUNT(1) FROM borrowers WHERE name ='"+str(username)
    zap+="';"
    czyjuzjest = cursor.execute(zap)
    if czyjuzjest is True:
        return "Użytkownik już istnieje."
    if password > 20:
        return "Prosze Podaj krótsze hasło"
    hashed_password = hash_password(password)
    zap = "INSERT INTO borrowers (borrower_id, name, email, phone,password) VALUES (,'"+str(username)+"','"+str(email)+"','"+str(telephone)+"','"+str(hashed_password)+"');"
    cursor.execute(zap)
    users_db[username] = hashed_password
    return "Rejestracja zakończona sukcesem!"

def login_user(username, password):
    """Funkcja logowania użytkownika."""

    # Tutaj będzie zapytanie do bazy danych. Można odrazu dać selecta i jeśli będzie pusty to zwrócić informację zły login lub hasło.
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
    # Tutaj będzie zapytanie do bazy danych.
    cursor = connection.cursor()
        # Połączenie z nowo utworzoną bazą danych
    if password > 20:
    	return "Podano Złe Hasło"
    #if username not in users_db:
    zap = "SELECT COUNT(1) FROM borrowers WHERE name ='"+str(username)
    zap+="';"
    odp = cursor.execute(zap)
    if odp == 0:
        return "Zły login"
    zap = "SELECT password FROM borrowers WHERE name ='"+str(username)
    zap+="';"
    hashed_password = cursor.execute(zap)
    if verify_password(password, hashed_password):
        return "Logowanie zakończone sukcesem!"
    else:
        return "Zły login lub hasło."

if __name__ == "__main__":
    while True:
        print("\n--- System logowania ---")
        print("1. Rejestracja")
        print("2. Logowanie")
        print("3. Wyjście")
        
        choice = input("Wybierz opcję: ")
        
        match choice:
            case "1":
                username = input("Podaj nazwę użytkownika: ")
                password = input("Podaj hasło: ")
                print(register_user(username, password))
            case "2":
                username = input("Podaj nazwę użytkownika: ")
                password = input("Podaj hasło: ")
                print(login_user(username, password))
            case "3":
                print("Do widzenia!")
                break
            case _:
                print("Nieprawidłowa opcja, spróbuj ponownie.")
