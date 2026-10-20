import mysql.connector

def database():
    connect = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="prompts"
    )

    if connect.is_connected():
        print("Conectado a la base de datos")
    else:
        print("No se pudo conectar a la base de datos")

    return connect
    
database()