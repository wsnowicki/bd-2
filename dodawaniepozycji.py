import os
#import psycopg2
#from psycopg2 import sql
#from dotenv import load_dotenv
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
            port=db_port)
cursor = connection.cursor()
print("Co chcesz dodac (1) Ksiazke (2)Autora (3)Gatunek (4) Dodaj Gatunek do ksiazki (x)Wyjdz")
x = input()
if str(x)=='1':
    titlek=input("podaj tytuł książki:")
    isbn=input("podaj tytuł kod ksiązki:")
    author=input("podaj autora książki:")
    rokwyd=input("podaj rok wydania książki:")
    temp = input("czy ksiązka jest już dostepna (T)ak")
    if str(temp)=="t" or str(temp)=="T":
        isactive=True
    else:
        isactive=False
    czymozna=True
    path=input("podaj nazw pliku po okladke")
    while(czymozna):
        zap = f"SELECT COUNT(1) FROM authors WHERE name ='{author}';"
        odp = cursor.execute(zap)
        czymozna=False
    	if str(odp) == "0":
    	    temp = input("Nowy Autor? (T)ak")
    	    if str(temp)=="t" or str(temp)=="T":
    	         zap = 'INSERT INTO authors (author_id, name) VALUES (,"'
                 zap += str(author)
                 zap+='");'
                 cursor.execute(zap)
            else:
                author=input("podaj autora książki:")
                czymozna=True
    getid=f"SELECT author_id FROM authors WHERE name ='{author}';"
    aid=cursor.execute(getid)       
    zap=f"INSERT INTO books (isbn, title, author_id, year_published,is_available,cover_image) VALUES ('{isbn}','{titlek}','{aid}','{rokwyd}','{isactive}','{}');"
    cursor.execute(zap)
elif str(x)=="2"
    Name = input("Podaj nazwe autora")
    zap = f"SELECT COUNT(1) FROM authors WHERE name ='{Name}';"
    odp = cursor.execute(zap)
    if str(odp)=='0':
        print("podany autor juz istnieje w bazie danych")
    else:
        zap = 'INSERT INTO authors (author_id, name) VALUES (,"'+str(Name)+"');"
        cursor.execute(zap)
elif str(x)=="3":
    genrename = input("Podaj nazwe nowego gatunku")
    newid=cursor.execute("SELECT COUNT(1) FROM genres")
    newid=newid+1
    zap=f"INSERT INTO genres (genre_id, name) VALUES ('{newid}','{genrename}');"
    cursor.execute("zap")
elif str(x)=="4":
    ksiag=input("podaj nazwe ksiazki")
    gatu=input("podaj jaki gatunek chcesz dodac")
    zap="SELECT COUNT(1) FROM genres WHERE name='"+str(gatu)+"';"
    odp = cursor.execute(zap)
    blad=False
    if str(odp)=='0':
        print("podany gatunek nie istnieje w bazie danych")
        blad=True
    zap="SELECT COUNT(1) FROM books WHERE title='"+str(ksiag)+"';"
    odp = cursor.execute(zap)
    if str(odp)=='0':
        print("podana ksiazka nie istnieje w bazie danych")
        blad=True
    if blad is False:
        zap = f"SELECT genre_id FROM genres WHERE name='{gatu}';"
        idk=cursor.execute(zap)
        zap = f"SELECT isbn FROM books WHERE title='{ksiag}';"
        idg=cursor.execute(zap)
        zap=f"SELECT COUNT(1) FROM books WHERE genre_id='{idk}' AND book_isbn='idg';"
        odp = cursor.execute(zap)
        if str(odp)=='0':
            zap=f"INSERT INTO book_genres (genre_id, book_isbn) VALUES ('{idk}','{idg}');"
            odp = cursor.execute(zap)
        else:
            print("Podana kombinacja jest juz w bazie danych")
else:
    print("nieprawidlowa opcja")

