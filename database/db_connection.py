import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="parola",
            database="my_database"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Eroare la conectare: {err}")
        return None
