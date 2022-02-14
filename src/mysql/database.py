import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def connect():
    connection = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        db="clientes",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield connection
    finally:
        connection.close()


with connect() as connection:
    with connection.cursor() as cursor:
        sql = "INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES " \
            "(%s, %s, %s, %s)"
        cursor.execute(sql, ("Jack", "Monroe", 112, 220))
        connection.commit()


with connect() as connection:
    with connection.cursor() as cursor:
        sql = "INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES " \
            "(%s, %s, %s, %s)"
        data = [
            ("Jack", "Silva", 112, 221),
            ("Jack", "Rouge", 113, 222),
            ("Jack", "Caria", 114, 223),
        ]
        cursor.execute(sql, data)
        connection.commit()


with connect() as connection:
    with connection.cursor() as cursor:
        sql = "DELETE FROM clientes WHERE id = %s"
        cursor.execute(sql, (6,))
        connection.commit()


with connect() as connection:
    with connection.cursor() as cursor:
        sql = "DELETE FROM clientes WHERE id IN (%s, %s, %s)"
        cursor.execute(sql, (7, 8, 9))
        connection.commit()


with connect() as connection:
    with connection.cursor() as cursor:
        sql = "DELETE FROM clientes WHERE id BETWEEN %s AND %s"
        cursor.execute(sql, (10, 12))
        connection.commit()


with connect() as connection:
    with connection.cursor() as cursor:
        sql = "UPDATE clientes SET nome=%s WHERE id=%s"
        cursor.execute(sql, ("JOANA", 5))
        connection.commit()


with connect() as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM clientes LIMIT 100")
        result = cursor.fetchall()

        print(result)


with connect() as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT nome, sobrenome FROM clientes ORDER BY id DESC LIMIT 100")
        result = cursor.fetchall()

        print(result)
