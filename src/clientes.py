import sqlite3
import getpass
import hashlib

# Função para inserir um novo cliente
def inserir_novo_cliente(conn):

    try:
        clientes_data = []

        #APAGAR NO FIM
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes;")
        clientes = cursor.fetchall()

        print("\nCLIENTES:")
        for cliente in clientes:
            print(cliente)
        #APAGAR NO FIM

        nome = input("CLIENTE\nNome: ")
        nif = input("NIF: ")
        email = input("Email: ")
        telefone = input("Telefone do cliente: ")
        password = getpass.getpass("Password: ")

        password_hash_cliente = hashlib.sha256(password.encode()).hexdigest()
                              #ID               NOME          EMAIL                    TELEFONE      PASSWORD
        clientes_data.append((nif,nome,email,telefone, password_hash_cliente))

        cursor.executemany("INSERT INTO clientes VALUES (?, ?, ?, ?, ?)", clientes_data)

    except sqlite3.IntegrityError as e:
        print("Ocorreu um erro. O cliente com o nif: '" + nif + "' já deve existir na BD.")
    
    conn.commit()

# Função para imprimir a lista de clientes
def imprime_lista_de_clientes(conn):
    try:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT nif, name, email, telefone, '*' || substr(password_hash, 2) as password_hidden FROM clientes;
        ''')

        clientes_all = cursor.fetchall()

        print(f"\nNIF |  NAME | EMAIL | TELEFONE | PASSWORD ")

        if clientes_all:
            print("")
            for i in clientes_all:
                print(f" {i[0]} | {i[1]} |  {i[2]} | {i[3]} ")
        else:
            print("Não existem clientes.")

        leave = input("\nClique qualquer botão para SAIR.")

    except sqlite3.Error as e:
        print(f"ERRO: a tabela não existe ou não existem registos")


#Ver informação de um cliente especifico
def select_informacao_cliente(conn, client_nif):
    try:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM clientes WHERE nif = ?;
        ''', (client_nif,))

        cliente_info = cursor.fetchone()

        if cliente_info:
            print("\nInformação do Cliente:")
            print(f"NIF: {cliente_info[0]}")
            print(f"Nome: {cliente_info[1]}")
            print(f"Email: {cliente_info[2]}")
            print(f"Telefone: {cliente_info[3]}\n")
           
        else:
            print(f"Cliente com NIF {client_nif} não encontrado.")

    except sqlite3.Error as e:
        print(f"Erro: {e}")


def select_informacao_empregado(conn, empregado_nif):
    try:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM empregados WHERE empregado_nif = ?;
        ''', (empregado_nif,))

        empregado_info = cursor.fetchone()

        if empregado_info:
            print("\nInformação do Empregado:")
            print(f"NIF: {empregado_info[0]}")
            print(f"Nome: {empregado_info[1]}")
            print(f"Email: {empregado_info[2]}")

           
        else:
            print(f"Empregado com NIF {empregado_nif} não encontrado.")

    except sqlite3.Error as e:
        print(f"Erro: {e}")
