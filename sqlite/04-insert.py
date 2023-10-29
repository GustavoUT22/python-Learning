import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        "insert into usuarios values(?, ?)",
        (1, "Hola Mundo"),
    )

    # solo pasemos los valores dentro de un segundo argumento
    # para prevenir sql injection == hackers
