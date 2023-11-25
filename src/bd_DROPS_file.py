import sqlite3

# CONEXAO
conn = sqlite3.connect('src/oficina.db')
cursor = conn.cursor()

# DROP TABLES
cursor.execute("DROP TABLE IF EXISTS Veiculos;")
cursor.execute("DROP TABLE IF EXISTS clientes;")
cursor.execute("DROP TABLE IF EXISTS faturas;")
cursor.execute("DROP TABLE IF EXISTS empregados;")


# COMMIT AND CLOSE CONNECTION
conn.commit()
conn.close()





