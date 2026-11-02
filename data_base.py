import sqlite3

def conectar():
    conexion = sqlite3.connect("prompts.db")
    cursor = conexion.cursor()

    # Crear las tablas necesarias si no existen
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS card (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt TEXT NOT NULL
        )
    """)
    conexion.commit()
    return conexion
