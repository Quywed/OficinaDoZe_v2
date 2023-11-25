import sqlite3

# Função para inserir um novo cliente
def inserir_novo_cliente(conn):
    """
    Insere um novo cliente na tabela 'clientes' do base de dados.

    :param conn: Conexão a base de dados.
    :type conn: sqlite3.Connection
    """

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
    """
    Imprime a lista de todos os clientes presentes na tabela 'clientes' do base de dados.

    :param conn: Conexão a base de dados.
    :type conn: sqlite3.Connection
    """

    try:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM clientes;
        ''')

        clientes_all= cursor.fetchall()

        print(f"\nNIF |  NAME | EMAIL | TELEFONE ")

        if clientes_all:
            print("")
            for i in clientes_all:
                print(f" {i[0]} | {i[1]} |  {i[2]} | {i[3]}")
        else:
            print("Não existem clientes.")

        leave = input("\nClique qualquer botão para SAIR.")

    except sqlite3.Error as e:
        print(f"Erro: {e}")
    