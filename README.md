# bd-2
Projekt z baz danych


## Uruchamianie
1. Utwórz bazę danych oraz użytkownika w postgresie
```sql
CREATE USER ubiblioteka WITH PASSWORD '123454321';
CREATE DATABASE biblioteka OWNER ubiblioteka;
\c biblioteka

-- Tabela książek
CREATE TABLE books (
    isbn VARCHAR(13) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT REFERENCES authors(author_id),
    genre VARCHAR(50),
    year_published INT,
    is_available BOOLEAN DEFAULT TRUE,
    cover_image BYTEA  -- Kolumna na okładkę książki
);
-- Tabela autorów
CREATE TABLE authors (
    author_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
-- Tabela wypożyczających
CREATE TABLE borrowers (
    borrower_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    phone VARCHAR(15)
);
-- Tabela wypożyczeń
CREATE TABLE loans (
    loan_id SERIAL PRIMARY KEY,
    book_id INT REFERENCES books(book_id),
    borrower_id INT REFERENCES borrowers(borrower_id),
    loan_date DATE DEFAULT CURRENT_DATE,
    return_date DATE,
    status VARCHAR(20) DEFAULT 'Wypożyczona'
);
```

2. Utwórz plik .env i wypełnij go odpowiednimi ustawieniami dla twoich potrzeb.
```bash
cp .env.example .env
vim .env
```

