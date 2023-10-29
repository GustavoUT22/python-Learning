import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (2, "llanero solitario"),
        (3, "lobo solitario")
    ]
    cursor.executemany(
        "insert into usuarios values(?, ?)",
        usuarios
    )
