import sqlite3


con = sqlite3.connect("sqlite/app.db")  # conectar base de datos
con.close()  # cerrar la conexion
