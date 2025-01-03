import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

# Wczytaj zmienne środowiskowe z pliku .env
load_dotenv()

def create_database():
    try:
        # Pobierz dane do połączenia z pliku .env
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST", "127.0.0.1")
        db_port = os.getenv("DB_PORT", "5432")
        initial_db = os.getenv("DB_INITIAL", "postgres")

        # Połączenie z PostgreSQL
        connection = psycopg2.connect(
            dbname=initial_db,  # Domyślna baza danych
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        connection.autocommit = True
        cursor = connection.cursor()

        # Tworzenie nowej bazy danych
        cursor.execute("CREATE DATABASE biblioteka;")
        print("Baza danych 'biblioteka' została utworzona.")

    except psycopg2.errors.DuplicateDatabase:
        print("Baza danych 'biblioteka' już istnieje.")
    finally:
        if connection:
            cursor.close()
            connection.close()

def create_tables():
    try:
        # Pobierz dane do połączenia z pliku .env
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST", "127.0.0.1")
        db_port = os.getenv("DB_PORT", "5432")
        db_name = os.getenv("DB_DATABASE", "biblioteka")

        # Połączenie z nowo utworzoną bazą danych
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        cursor = connection.cursor()

        # Tworzenie tabel
        cursor.execute("""
            CREATE TABLE borrowers (
                borrower_id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255),
                phone VARCHAR(15)
            );

            CREATE TABLE status (
                id SERIAL PRIMARY KEY,
                status VARCHAR(64),
                description VARCHAR(255)
            );

            CREATE TABLE authors (
                author_id SERIAL PRIMARY KEY,
                name VARCHAR(255), NOT NULL
            );

            CREATE TABLE books (
                isbn VARCHAR(13) PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author_id INTEGER REFERENCES authors(author_id),
                year_published INTEGER,
                is_available BOOLEAN DEFAULT TRUE,
                cover_image BYTEA
            );

            CREATE TABLE loans (
                loan_id SERIAL PRIMARY KEY,
                book_id VARCHAR(13) REFERENCES books(isbn),
                borrower_id INTEGER REFERENCES borrowers(borrower_id),
                loan_date DATE DEFAULT CURRENT_DATE,
                return_date DATE,
                status INTEGER REFERENCES status(id)
            );

            CREATE TABLE genres (
                genre_id INTEGER PRIMARY KEY,
                name VARCHAR(50) UNIQUE
            );

            CREATE TABLE book_genres (
                genre_id INTEGER REFERENCES genres(genre_id),
                book_isbn VARCHAR(13) REFERENCES books(isbn),
                PRIMARY KEY (genre_id, book_isbn)
            );
        """)
        print("Tabele zostały utworzone pomyślnie.")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
    create_tables()

