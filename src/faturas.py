from datetime import date
import sqlite3

nome_ficheiro_lista_de_faturas = "lista_de_faturas.pk"

def cria_nova_fatura(cliente_nif, descricao, valor):
    """
    Cria uma nova fatura no banco de dados.

    :param cliente_nif: NIF do cliente associado à fatura.
    :type cliente_nif: int
    :param descricao: Descrição da fatura.
    :type descricao: str
    :param valor: Valor da fatura.
    :type valor: float
    """

    conn = sqlite3.connect('src/oficina.db')
    cursor = conn.cursor()

    data_criacao = datetime.now()

    cursor.execute("INSERT INTO faturas (cliente_nif, data_criacao, descricao, valor) VALUES (?, ?, ?, ?)",
                   (cliente_nif, data_criacao, descricao, valor))

    conn.commit()
    conn.close()

def imprime_lista_de_faturas():
    """
    Imprime a lista de todas as faturas presentes no banco de dados.
    """
    conn = sqlite3.connect('src/oficina.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM faturas")
    faturas = cursor.fetchall()

    print("\nFATURAS:")
    for fatura in faturas:
        print(fatura)

    conn.close()


