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
# import psycopg2
from enum import Enum, auto
import random, string


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

def register_user(conn, username: str, password: str, email: str,telephone: str):
    """Funkcja rejestrująca użytkownika."""
    cursor = conn.cursor()

    zap = f"SELECT COUNT(1) FROM borrowers WHERE name ='{username}';"
    czyjuzjest = cursor.execute(zap)
    if czyjuzjest is True:
        return Status.USER_EXISTS

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
    cursor = conn.cursor()

    zap = f"SELECT password FROM borrowers WHERE name ='{username}';"
    cursor.execute(zap)
    hashed_password = cursor.fetchone()
    if hashed_password is None: return Status.WRONG_LOGIN

    if isinstance((hashed_password := hashed_password[0]), str):
        hashed_password = hashed_password.encode('utf-8')


    if hashed_password is None:
        return Status.WRONG_LOGIN

    if verify_password(password, hashed_password):
        return Status.OK
    else:
        return Status.WRONG_LOGIN


# Funkcja do generowania losowego stringa o zadanej długości
def generate_random_string(length=8):
    characters = string.ascii_letters + string.digits  # Wszystkie litery i cyfry
    return ''.join(random.choice(characters) for _ in range(length))


if __name__ == "__main__":
    stringi = [generate_random_string(12) for _ in range(10)]
    hashed = [encrypt_password(s) for s in stringi]
    print(stringi)
    print(hashed)




