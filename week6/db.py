from fastapi import Depends
import mysql.connector

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "test",
            database = "website"
        )
        print("Database connection successful")
    except mysql.connector.Error as err:
        print(f'Database connection failed: {err}')
        raise
    return connection

def get_db():
    connection = get_db_connection()
    db = connection.cursor( buffered=True )

    try:
        yield db
    finally:
        db.close()
        connection.close()

def query_user(username , password):
    db_generator = get_db()
    db = next(db_generator)

    try:
        query = "select * from member where username = %s and password = %s"
        db.execute(query , (username , password))
        result = db.fetchone()
        if result:
            print("User Found:" , result)
        else:
            print("No user found with the provided username and password")
    finally:
        next(db_generator , None)


if __name__ == "__main__":
    query_user("test" , "test")