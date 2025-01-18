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

users_db = {}

def encrypt_password(password):
    """Funkcja do szyfrowania hasła."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def verify_password(password, hashed):
    """Funkcja do weryfikacji hasła."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def register_user(username, password):
    """Funkcja rejestrująca użytkownika."""

    # Tutaj będzie zapytanie do bazy danych.
    if username in users_db:
        return "Użytkownik już istnieje."
    
    hashed_password = hash_password(password)
    users_db[username] = hashed_password
    return "Rejestracja zakończona sukcesem!"

def login_user(username, password):
    """Funkcja logowania użytkownika."""

    # Tutaj będzie zapytanie do bazy danych. Można odrazu dać selecta i jeśli będzie pusty to zwrócić informację zły login lub hasło.
    if username not in users_db:
        return "Zły login lub hasło."
    
    hashed_password = users_db[username]
    if verify_password(password, hashed_password):
        return "Logowanie zakończone sukcesem!"
    else:
        return "Zły login lub hasło."

if __name__ == "__main__":
    # Test szyfrowania hasła
    password = "tajnehaslo"
    hashed = encrypt_password(password)
    print(hashed)
    print(verify_password(password, hashed[:-2]))