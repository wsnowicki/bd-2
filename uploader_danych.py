import json
import os
#import psycopg2
#from psycopg2 import sql
#from dotenv import load_dotenv
def insert_values_into_db():
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
        f = open('mockdata/borrowers.json')
        data = json.load(f)
        for i in data['borrowers']:
            zap = 'INSERT INTO borrowers (borrower_id, name, email, phone) VALUES ("'
            zap += str(i['borrower_id'])
            zap+='","'
            zap += str(i['name'])
            zap+='","'
            zap += str(i['email'])
            zap+='","'
            zap += str(i['phone'])
            zap+='");'
            print(zap)
            #cursor.execute(zap)
        f.close()
        
        f = open('mockdata/authors.json')
        data = json.load(f)
        for i in data['authors']:
            zap = 'INSERT INTO authors (author_id, name) VALUES ("'
            zap += str(i['author_id'])
            zap+='","'
            zap += str(i['name'])
            zap+='");'
            print(zap)
            #cursor.execute(zap)
        f.close()
        
        f = open('mockdata/status.json')
        data = json.load(f)
        for i in data['status']:
                
            zap = 'INSERT INTO status (id, status,description) VALUES ("'
            zap += str(i['id'])
            zap+='","'
            zap += str(i['status'])
            zap+='","'
            zap += str(i['description'])
            zap+='");'
            print(zap)
            #cursor.execute(zap)
        f.close()
        f = open('mockdata/loans.json')
        data = json.load(f)
        for i in data['loans']:
                
            zap = 'INSERT INTO loans (loan_id, book_id,borrower_id,loan_date,return_date,status) VALUES ("'
            zap += str(i['loan_id'])
            zap+='","'
            zap += str(i['book_id'])
            zap+='","'
            zap += str(i['borrower_id'])
            zap+='","'
            zap += str(i['loan_date'])
            zap+='","'
            zap += str(i['return_date'])
            zap+='","'
            zap += str(i['status'])
            zap+='");'
            print(zap)
            #cursor.execute(zap)
        f.close()
        f = open('mockdata/genres.json')
        data = json.load(f)
        for i in data['genres']:
                
            zap = 'INSERT INTO genres (genre_id, name) VALUES ("'
            zap += str(i['genre_id'])
            zap+='","'
            zap += str(i['name'])
            zap+='");'
            print(zap)
            #cursor.execute(zap)
        f.close()
        f = open('mockdata/book_genres.json')
        data = json.load(f)
        for i in data['book_genres']:
                
            zap = 'INSERT INTO book_genres (genre_id, book_isbn) VALUES ("'
            zap += str(i['genre_id'])
            zap+='","'
            zap += str(i['book_isbn'])
            zap+='");'
            print(zap)
            #cursor.execute(zap)
        f.close()
        f = open('mockdata/book.json')
        data = json.load(f)
        for i in data['books']:
            zap = 'INSERT INTO books (isbn, title, author_id, year_published,is_available,cover_image) VALUES ("'
            zap += str(i['isbn'])
            zap+='","'
            zap += str(i['title'])
            zap+='","'
            zap += str(i['author_id'])
            zap+='","'
            zap += str(i['year_published'])
            zap+='","'
            zap += str(i['is_available'])
            zap+='","'
            img=str(i['cover_image'])
            with open(f"mockdata/photos/pobrany_{img}", "rb") as file:
            	zap+=str(file.read())
            zap+='");'
            #print(zap)
            #cursor.execute(zap)
            file.close()
        f.close()
        
        
        
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    finally:
        pass
        #if connection:
        #    cursor.close()
        #    connection.close()
if __name__ == "__main__":
    insert_values_into_db()
