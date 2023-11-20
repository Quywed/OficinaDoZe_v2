import sqlite3

# Função para criar a tabela de clientes
def criar_tabela_clientes():
    conn = sqlite3.connect('src/oficina.db')  # Conecta ao banco de dados (cria se não existir)
    cursor = conn.cursor()

    # Cria uma tabela de clientes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            nif TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    ''')
    
    conn.commit()  # Salva as alterações
    conn.close()   # Fecha a conexão

# Função para inserir um novo cliente
def inserir_novo_cliente(cliente):
    conn = sqlite3.connect('src/oficina.db')
    cursor = conn.cursor()

    # Insere um novo cliente na tabela
    cursor.execute('''
        INSERT INTO cliente (nome, nif, email, telefone)
        VALUES (?, ?, ?, ?)
    ''', (cliente['nome'], cliente['nif'], cliente['email'], cliente['telemovel']))
    
    conn.commit()
    conn.close()

# Função para imprimir a lista de clientes
def imprime_lista_de_clientes():
    conn = sqlite3.connect('src/oficina.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM clientes')
    lista_de_clientes = cursor.fetchall()

    if not lista_de_clientes:
        print("A lista de clientes está vazia.")
        return

    print("Lista de Clientes:")
    for cliente in lista_de_clientes:
        print(f"ID: {cliente[0]}")
        print(f"Nome: {cliente[1]}")
        print(f"NIF: {cliente[2]}")
        print(f"E-mail: {cliente[3]}")
        print(f"telemovel: {cliente[4]}")
        print("-" * 20)

    conn.close()