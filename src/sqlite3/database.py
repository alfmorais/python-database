import sqlite3
import os


filename = r"database.py"


# abre o banco de dados e cria um cursor para persistir os dados
connection = sqlite3.connect("database.db")
cur = connection.cursor()


if filename is False:
    # cria uma tabela que chama clientes com as colunas id, nome e peso.
    cur.execute(
        'CREATE TABLE IF NOT EXISTS clientes ('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'nome TEXT,'
        'peso REAL'
        ')'
    )


    # inserindo dados no banco de dados
    cur.execute(
        'INSERT INTO clientes (nome, peso) VALUES ("Alfredo de Morais", 65.50)'
    )
    cur.execute(
        'INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Joaquim', 7.5)
    )
    cur.execute(
        'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
        {
            "nome": "Denise",
            "peso": 78.5
        }
    )
    cur.execute(
        'INSERT INTO clientes VALUES (:id, :nome, :peso)',
        {
            "id": None,
            "nome": "Vera",
            "peso": 75.4
        }
    )
    connection.commit()


# mostrando todos os dados de uma tabela
cur.execute(
    'SELECT * FROM clientes'
)

# interando os dados de uma tabela
for linha in cur.fetchall():
    identification, name, weight = linha
    print(identification, name, weight)


# atualizando dados da tabela
cur.execute(
    'UPDATE clientes SET nome=:nome WHERE id=:id',
    {
        "id": 2,
        "nome": "Joaquim Neto"
    }
)
connection.commit()


# mostrando todos os dados de uma tabela
cur.execute(
    'SELECT * FROM clientes'
)

# interando os dados de uma tabela
for linha in cur.fetchall():
    identification, name, weight = linha
    print(identification, name, weight)


# deletando dados de uma tabela
cur.execute(
    'DELETE FROM clientes WHERE id=:id',
    {"id": 4}
)

# boa prática em bancos de dados, abrir e fechar -> conexão e cursor.
cur.close()
connection.close()


# filtrando dados de uma tabela com WHERE
# cur.execute('SELECT nome, peso FROM clientes WHERE peso > 50')
# cur.execute('SELECT nome, peso FROM clientes WHERE peso > :peso', {"peso": 50})