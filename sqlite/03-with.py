import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()  # intermediario entre nostros y sqlite3 para hacer consultas
    cursor.execute(
        """
        CREATE TABLE if not exists usuarios
        (id INTEGER primary key, nombre VARCHAR(50));
        """
    )
