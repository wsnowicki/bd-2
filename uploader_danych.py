import json
import os
#import psycopg2
#from psycopg2 import sql
#from dotenv import load_dotenv
def insert_values_into_db():
    try:
        # Pobierz dane do połączenia z pliku .env
        #db_user = os.getenv("DB_USER")
        #db_password = os.getenv("DB_PASSWORD")
        #db_host = os.getenv("DB_HOST", "127.0.0.1")
        #db_port = os.getenv("DB_PORT", "5432")
        #db_name = os.getenv("DB_DATABASE", "biblioteka")

        # Połączenie z nowo utworzoną bazą danych
        #connection = psycopg2.connect(
        #    dbname=db_name,
        #    user=db_user,
        #    password=db_password,
        #    host=db_host,
        #    port=db_port
        #)
        #cursor = connection.cursor()
        f = open('mockdata/dane.json')
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
        
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    finally:
        pass
        #if connection:
        #    cursor.close()
        #    connection.close()
if __name__ == "__main__":
    insert_values_into_db()
