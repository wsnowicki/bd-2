import psycopg2

try:
    # Połączenie z bazą danych
    conn = psycopg2.connect(
        dbname="biblioteka",
        user="ubiblioteka",
        password="123454321",
        host="127.0.0.1",
        port="5432"
    )
    cur = conn.cursor()

    # Dodawanie autorów
    cur.execute("INSERT INTO authors (author_id, name) VALUES (1, 'Pablusz Gumoleusz');")
    cur.execute("INSERT INTO authors (author_id, name) VALUES (2, 'Wincenty Przekichacz');")
    cur.execute("INSERT INTO authors (author_id, name) VALUES (3, 'Linus Jabłko');")

    # Dodawanie gatunków
    cur.execute("INSERT INTO genres (genre_id, name) VALUES (1, 'Western');")
    cur.execute("INSERT INTO genres (genre_id, name) VALUES (2, 'Poradnik');")
    cur.execute("INSERT INTO genres (genre_id, name) VALUES (3, 'Science-fiction');")

    # Odczyt obrazu
    with open("image1.png", "rb") as file:
        bity = file.read()

    # Dodawanie książek
    books = [
        (322421, 'o trzech takich co wynaleźli UML-a', 1, 2020, True, bity),
        (322420, 'Czy Studia się opłacają?', 2, 2024, True, bity),
        (322429, 'Spóźnialska Asia', 3, 2023, True, bity),
        (322428, 'Half-life 3 na tropie legnedy', 1, 1999, True, bity)
    ]

    for book in books:
        cur.execute(
            """
            INSERT INTO books (isbn, title, author_id, year_published, is_available, cover_image)
            VALUES (%s, %s, %s, %s, %s, %s);
            """,
            book
        )

    # Dodawanie powiązań książek z gatunkami
    book_genres = [
        (1, 322421),
        (2, 322420),
        (1, 322429),
        (3, 322428)
    ]

    for genre in book_genres:
        cur.execute(
            "INSERT INTO book_genres (genre_id, book_isbn) VALUES (%s, %s);",
            genre
        )

    # Dodawanie statusów
    cur.execute(
        """
        INSERT INTO status (id, status, description)
        VALUES (1, 'aktywna', 'ksiazka moze byc wypożyczona');
        """
    )

    # Dodawanie użytkowników
    cur.execute(
        """
        INSERT INTO borrowers (borrower_id, name, email, phone)
        VALUES (1, 'JanKonstantynoopol', 'ista@gmail.com', '434313333');
        """
    )

    # Dodawanie wypożyczeń
    cur.execute(
        """
        INSERT INTO loans (loan_id, book_id, borrower_id, loan_date, return_date, status)
        VALUES (1, 322421, 1, '2024-02-02', '2024-03-03', 1);
        """
    )

    # Zatwierdzanie zmian
    conn.commit()
    print("Dane zostały pomyślnie dodane.")

except psycopg2.Error as e:
    print(f"Wystąpił błąd: {e}")
    conn.rollback()

finally:
    # Zamknięcie kursora i połączenia
    if cur:
        cur.close()
    if conn:
        conn.close()

