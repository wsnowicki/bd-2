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
from enum import Enum, auto


load_dotenv()

http_host = getenv("HTTP_HOST")
http_port = getenv("HTTP_PORT")
http_threads = getenv("HTTP_THREADS")


class Status(Enum):
    OK = auto()
    USER_EXISTS = auto()
    PASSWORD_TOO_LONG = auto()
    WRONG_LOGIN = auto()


def encrypt_password(password):
    """Funkcja do szyfrowania hasła."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def verify_password(password, hashed):
    """Funkcja do weryfikacji hasła."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def register_user(conn, username: str, password: str):
    """Funkcja rejestrująca użytkownika."""

    email='testowy@gmail'
    telephone='111333222'

    # db_user = getenv("DB_USER")
    # db_password = getenv("DB_PASSWORD")
    # db_host = getenv("DB_HOST", "127.0.0.1")
    # db_port = getenv("DB_PORT", "5432")
    # db_name = getenv("DB_DATABASE", "biblioteka")
    # conn = psycopg2.connect(
    #     dbname=db_name,
    #     user=db_user,
    #     password=db_password,
    #     host=db_host,
    #     port=db_port
    # )
    cursor = conn.cursor()
    
    zap = f"SELECT COUNT(1) FROM borrowers WHERE name ='{username}';"
    czyjuzjest = cursor.execute(zap)
    if czyjuzjest is True:
        return Status.USER_EXISTS
    if password > 20:
        return Status.PASSWORD_TOO_LONG
    
    hashed_password = hash_password(password)
    # zap = "INSERT INTO borrowers (borrower_id, name, email, phone,password) VALUES (,'"+username+"','"+email+"','"+telephone+"','"+hashed_password+"');"
    zap = f"""
    INSERT INTO borrowers (borrower_id, name, email, phone, password) 
    VALUES (NULL, '{username}', '{email}', '{telephone}', '{hashed_password}');
    """
    cursor.execute(zap)

    return Status.OK

def login_user(conn, username, password):
    """Funkcja logowania użytkownika."""

    if password > 20:
        return Status.PASSWORD_TOO_LONG

    cursor = conn.cursor()

    zap = f"SELECT password FROM borrowers WHERE name ='{username}';"
    odp = cursor.execute(zap)
    hashed_password = odp.fetchone()
    if hashed_password is None:
        return Status.WRONG_LOGIN

    if verify_password(password, hashed_password):
        return Status.OK
    else:
        return Status.WRONG_LOGIN





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
