import sqlite3

def dropping_bd(conn):
    """Elimina as tabelas existentes na base de dados.

    Esta função estabelece ligação à base de dados SQLite 'oficina.db' localizada no diretório 'src'
    e elimina as seguintes tabelas caso existam: Veiculos, clientes, faturas, empregados.

    :param conn: Conexão ativa com a base de dados SQLite.
    :type conn: sqlite3.Connection
    Raises:
        OperationalError: If there's an issue while dropping the tables.

    Returns:
        None
    
    """
    
    # CONEXAO
    cursor = conn.cursor()

    # DROP TABLES
    cursor.execute("DROP TABLE IF EXISTS Veiculos;")
    cursor.execute("DROP TABLE IF EXISTS clientes;")
    cursor.execute("DROP TABLE IF EXISTS faturas;")
    cursor.execute("DROP TABLE IF EXISTS empregados;")


    # COMMIT AND CLOSE CONNECTION
    conn.commit()
    conn.close()

conn = sqlite3.connect('src/oficina.db')
dropping_bd(conn)