from fastapi import Depends
import mysql.connector
import logging

# 創建文件處理程序
file_handler = logging.FileHandler(filename='app.log')
file_handler.setLevel(logging.INFO)

# 創建控制台處理程序
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 創建日誌器並添加處理
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(console_handler)


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
                   select message.id as message_id , member.id as member_id , member.name , message.content
                   from message
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

def insert_message(member_id , content):
    connection = get_db_connection()
    try:
        db = connection.cursor( dictionary = True )
        db.execute("insert into message (member_id , content) values (%s , %s )" , (member_id , content)) 
        connection.commit()
        logging.info(f"User {member_id} successfully added message:  {content}")
    except Exception as e:
        logging.error(f"Error saving message: {e} ")

    finally:
        db.close()
        connection.close()

def is_user_message_owner(user_id , message_id):
    connection = get_db_connection()
    try:
        db = connection.cursor( dictionary = True )
        db.execute("select id from message where member_id= %s and id= %s" , (user_id , message_id)) 
        message = db.fetchone()
        return bool(message)
    
    except Exception as e:
        logging.error(f"Error verifing message owner: {e} ")
        return False

    finally:
        db.close()
        connection.close()


def delete_message(message_id):
    connection = get_db_connection()
    try:
        db = connection.cursor()
        db.execute("delete from message where id= %s" , (message_id,)) 
        connection.commit()
        logging.info(f"User successfully delete message id : {message_id}")
    except Exception as e:
        logging.error(f"Error deleting message: {e} ")

    finally:
        db.close()
        connection.close()

if __name__ == "__main__":
    pass