import sqlite3

# Função para inserir um novo cliente
def inserir_novo_cliente(conn):

    cursor = conn.cursor()

    nome = input("Nome do cliente: ")
    nif = input("NIF do cliente: ")
    email = input("E-mail do cliente: ")
    telefone = input("Telefone do cliente: ")

    cursor.execute('''
        INSERT INTO clientes (nome, nif, email, telefone)
        VALUES (?, ?, ?, ?)
    ''', (nome, nif, email, telefone))
    
    conn.commit()
    conn.close()

# Função para imprimir a lista de clientes
def imprime_lista_de_clientes(conn):

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