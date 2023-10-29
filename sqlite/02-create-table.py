import sqlite3

con = sqlite3.connect("sqlite/app.db")
cursor = con.cursor()  # intermediario entre nostros y sqlite3 para hacer consultas
cursor.execute(
    """
    CREATE TABLE if not exists usuarios
    (id INTEGER primary key, nombre VARCHAR(50));
    """
)

con.commit()  # comprometemos los cambios
con.close()
