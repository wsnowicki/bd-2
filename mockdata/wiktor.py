import psycopg2
conn = psycopg2.connect(
    dbname="biblioteka",
    user="ubiblioteka",
    password="123454321",
    host="127.0.0.1",
    port="5432"
)
cur = conn.cursor()
cur.execute("INSERT INTO authors (author_id, name) VALUES ('1','Pablusz Gumoleusz');")
cur.execute("INSERT INTO authors (author_id, name) VALUES ('2','Wincenty Przekichacz');")
cur.execute("INSERT INTO authors (author_id, name) VALUES ('3','Linus Jabłko');")
cur.execute("INSERT INTO genres (genre_id, name) VALUES ('1','Western');")
cur.execute("INSERT INTO genres (genre_id, name) VALUES ('2','Poradnik');")
cur.execute("INSERT INTO genres (genre_id, name) VALUES ('3','Science-fiction');")
with open(f"image1", "wb") as file:
    bity=file.read()
zap = f"INSERT INTO books (isbn, title, author_id, year_published,is_available,cover_image) VALUES ('322421','o trzech takich co wynaleźli UML-a','1','2020','1','{str(bity)}'"
cur.execute(zap)
zap= f"INSERT INTO books (isbn, title, author_id, year_published,is_available,cover_image) VALUES ('322420','Czy Studia się opłacają?','2','2024','1','{str(bity)}'"
cur.execute(zap)
zap= f"INSERT INTO books (isbn, title, author_id, year_published,is_available,cover_image) VALUES ('322429','Spóźnialska Asia','3','2023','1','{str(bity)}'"
cur.execute(zap)
zap= f"INSERT INTO books (isbn, title, author_id, year_published,is_available,cover_image) VALUES ('322428','Half-life 3 na tropie legnedy','1','1999','1','{str(bity)}'"
cur.execute(zap)
cur.execute("INSERT INTO book_genres (genre_id, book_isbn) VALUES ('1','322421');")
cur.execute("INSERT INTO book_genres (genre_id, book_isbn) VALUES ('2','322420');")
cur.execute("INSERT INTO book_genres (genre_id, book_isbn) VALUES ('1','322429');")
cur.execute("INSERT INTO book_genres (genre_id, book_isbn) VALUES ('3','322428');")
cur.execute("INSERT INTO status (id, status,description) VALUES ('1','aktywna','ksiazka moze byc wypożyczona');")
cur.execute("INSERT INTO borrowers (borrower_id, name, email, phone) VALUES ('1','JanKonstantynoopol','ista@gmail.com','434313333','$2b$12$1524k/s0ywdRTu3YFuBJ7eJFHvg3ALpThq8.GAB1L31CJk9XSZ4ju');")


cur.execute("INSERT INTO loans (loan_id, book_id,borrower_id,loan_date,return_date,status) VALUES ('1','322421','1','02-02-2024','03-03-2024','1');")

