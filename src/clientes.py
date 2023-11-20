import sqlite3

# Função para inserir um novo cliente
def inserir_novo_cliente(conn):

    cursor = conn.cursor()

    nome = input("Nome do cliente: ")
    nif = input("NIF do cliente: ")
    email = input("E-mail do cliente: ")
    telefone = input("Telefone do cliente: ")

    cursor.execute('''
        INSERT INTO clientes (nif, name, email, telefone)
        VALUES (?, ?, ?, ?)
    ''', (nif, nome, email, telefone))
    
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
        print(f"Nome: {cliente['nome']}")
        print(f"NIF: {cliente['nif']}")
        print(f"E-mail: {cliente['email']}")
        print(f"Telemovel: {cliente['telemovel']}")
        print("-" * 20)  # Linha separadora entre os clientes

#

