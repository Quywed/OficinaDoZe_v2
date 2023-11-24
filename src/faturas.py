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

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM faturas WHERE cliente_nif = ?", (cliente_nif,))
    faturas_cliente = cursor.fetchall()

    print(f"\nFATURAS DO CLIENTE {cliente_nif}:")
    for fatura in faturas_cliente:
        print(fatura)

    conn.close()