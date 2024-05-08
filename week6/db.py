from fastapi import Depends
import mysql.connector
import logging

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

def check_username_exists(register_username):
    connection = get_db_connection()
    try:
        db = connection.cursor()
        db.execute("select username from member where username = %s" , (register_username,))
        user = db.fetchone()
    finally:
        db.close()
        connection.close()
    
    return user is not None

def insert_new_user(name , register_username , register_password):
    connection = get_db_connection()
    try:
        db = connection.cursor()
        db.execute("insert into member (name , username , password) values (%s , %s , %s)" , (name , register_username , register_password))
        connection.commit()
        logging.info("User successfully added: %s" , register_username)
    except Exception as e:
        logging.error("Failed to add user: %s" , e)
        return False
    finally:
        db.close()
        connection.close()
    return True

def check_username(username , password):
    connection = get_db_connection()
    try:
        db = connection.cursor( dictionary = True )
        db.execute("select * from member where username = %s and password = %s " , ( username , password ))
        user_record = db.fetchone()
        return user_record
    
    except Exception as e:
        logging.error(f"Database error: {e} ")
        return False

    finally:
        db.close()
        connection.close()

def get_all_messages():
    connection = get_db_connection()
    try:
        db = connection.cursor( dictionary = True )
        db.execute("""
                   select member.name , message.content from message
                   join member on  message.member_id = member.id
                   order by message.time desc
                   """)
        return db.fetchall()
    
    except Exception as e:
        logging.error(f"Error retrieving message: {e} ")
        return []

    finally:
        db.close()
        connection.close()

def save_message(member_id , content):
    connection = get_db_connection()
    try:
        db = connection.cursor( dictionary = True )
        db.execute("insert into message (member_id , content) values (%s , %s )" , (member_id , content)) 
        connection.commit()
    
    except Exception as e:
        logging.error(f"Error saving message: {e} ")

    finally:
        db.close()
        connection.close()


if __name__ == "__main__":
    pass