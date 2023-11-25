from datetime import datetime
import sqlite3


def cria_nova_fatura(conn):
    """
    Cria uma nova fatura na base de dados.

    :param conn: Conexão ativa com a base de dados SQLite.
    :type conn: sqlite3.Connection
    """

    cursor = conn.cursor()

    cliente_nif = int(input("NIF Cliente: "))  
    descricao = input("Descrição da Fatura: ")
    valor = input("Valor da Fatura: ")
    
    data_criacao = datetime.now()

    cursor.execute("INSERT INTO faturas (cliente_nif, data_criacao, descricao, valor) VALUES (?, ?, ?, ?)",
                   (cliente_nif, data_criacao, descricao, valor))

    conn.commit()

def imprime_lista_de_faturas(conn):
    """
    Imprime a lista de todas as faturas presentes na base de dados.

    :param conn: Conexão ativa com a base de dados SQLite.
    :type conn: sqlite3.Connection
    """
    conn = sqlite3.connect('src/oficina.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM faturas")
    faturas = cursor.fetchall()

    print("\nFATURAS:")
    for fatura in faturas:
        print(fatura)



def faturas_cliente(conn, cliente_nif):
    """Seleciona e exibe as faturas de um cliente baseado no NIF.

    Esta função realiza uma consulta na tabela 'faturas' da base de dados utilizando o número de identificação
    fiscal (NIF) fornecido como argumento e exibe as faturas relacionadas ao cliente se elas existirem.

    Args:
        conn: Objeto de conexão com a base de dados.
        cliente_nif: NIF do cliente para o qual as faturas serão pesquisadas.

    Returns:
        None
    """

    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM faturas WHERE cliente_nif = ?", (cliente_nif,))
            faturas_cliente = cursor.fetchall()

            if faturas_cliente:
                print(f"\nFATURAS DO CLIENTE {cliente_nif}:")

                # Print header
                print(f"{'ID': <5}" + " | " +  f"{'DATA CRIAÇÃO': <15}" + " | " + f"{'DESCRIÇÃO': <30}" + " | " + f"{'VALOR': <10}\n")

                # Print each invoice
                for fatura in faturas_cliente:
                    print(f"{fatura[0]: <5}" + " | " + f"{fatura[2]: <15}" + " | " + f"{fatura[3]: <30}" +  " | " + f"{fatura[4]: <10}")
            else:
                print(f"Não existem faturas para o cliente {cliente_nif}.")

    except sqlite3.Error as e:
        print(f"Erro: {e}")