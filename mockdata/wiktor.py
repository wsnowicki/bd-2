import psycopg2
conn = psycopg2.connect(
    dbname="twoja_baza",
    user="twoj_user",
    password="twoje_haslo",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
cursor.execute("INSERT INTO authors (author_id, name) VALUES ('1','Pablusz Gumoleusz');")
cursor.execute("INSERT INTO authors (author_id, name) VALUES ('2','Wincenty Przekichacz');")
cursor.execute("INSERT INTO authors (author_id, name) VALUES ('3','Linus Jabłko');")
cursor.execute("INSERT INTO genres (genre_id, name) VALUES ('1','Western');")
cursor.execute("INSERT INTO genres (genre_id, name) VALUES ('2','Poradnik');")
cursor.execute("INSERT INTO genres (genre_id, name) VALUES ('3','Science-fiction');")
zap = f"INSERT INTO books (isbn, title, author_id, year_published,is_available,cover_image) VALUES ('322421','o trzech takich co wynaleźli UML-a','1','2020','1','{str(bity)}'"
cursor.execute(zap)
zap= f"INSERT INTO books (isbn, title, author_id, year_published,is_available,cover_image) VALUES ('322420','Czy Studia się opłacają?','2','2024','1','{str(bity)}'"
cursor.execute(zap)
zap= f"INSERT INTO books (isbn, title, author_id, year_published,is_available,cover_image) VALUES ('322429','Spóźnialska Asia','3','2023','1','{str(bity)}'"
cursor.execute(zap)
zap= f"INSERT INTO books (isbn, title, author_id, year_published,is_available,cover_image) VALUES ('322428','Half-life 3 na tropie legnedy','1','1999','1','{str(bity)}'"
cursor.execute(zap)
cursor.execute("INSERT INTO book_genres (genre_id, book_isbn) VALUES ('1','322421');")
cursor.execute("INSERT INTO book_genres (genre_id, book_isbn) VALUES ('2','322420');")
cursor.execute("INSERT INTO book_genres (genre_id, book_isbn) VALUES ('1','322429');")
cursor.execute("INSERT INTO book_genres (genre_id, book_isbn) VALUES ('3','322428');")
cursor.execute("INSERT INTO status (id, status,description) VALUES ('1','aktywna','ksiazka moze byc wypożyczona');")
cursor.execute("INSERT INTO borrowers (borrower_id, name, email, phone) VALUES ('1','JanKonstantynoopol','ista@gmail.com','434313333','$2b$12$1524k/s0ywdRTu3YFuBJ7eJFHvg3ALpThq8.GAB1L31CJk9XSZ4ju');")
with open(f"image1", "wb") as file:
    bity=file.read()

cursor.execute("INSERT INTO loans (loan_id, book_id,borrower_id,loan_date,return_date,status) VALUES ('1','322421','1','02-02-2024','03-03-2024','1');")

