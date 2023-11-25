from datetime import datetime
import sqlite3


def cria_nova_fatura(conn):
    cursor = conn.cursor()

    cliente_nif = int(input("NIF Cliente: "))  
    descricao = input("Descrição da Fatura: ")
    valor = input("Valor da Fatura: ")
    
    data_criacao = datetime.now()

    cursor.execute("INSERT INTO faturas (cliente_nif, data_criacao, descricao, valor) VALUES (?, ?, ?, ?)",
                   (cliente_nif, data_criacao, descricao, valor))

    conn.commit()

def imprime_lista_de_faturas(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM faturas")
    faturas = cursor.fetchall()

    print("\nFATURAS:")
    for fatura in faturas:
        print(fatura)



def faturas_cliente(conn, cliente_nif):
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