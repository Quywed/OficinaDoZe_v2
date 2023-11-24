from datetime import date

nome_ficheiro_lista_de_faturas = "lista_de_faturas.pk"

def cria_nova_fatura(cliente_nif, descricao, valor):
    conn = sqlite3.connect('src/oficina.db')
    cursor = conn.cursor()

    data_criacao = datetime.now()

    cursor.execute("INSERT INTO faturas (cliente_nif, data_criacao, descricao, valor) VALUES (?, ?, ?, ?)",
                   (cliente_nif, data_criacao, descricao, valor))

    conn.commit()
    conn.close()

def imprime_lista_de_faturas():
    conn = sqlite3.connect('src/oficina.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM faturas")
    faturas = cursor.fetchall()

    print("\nFATURAS:")
    for fatura in faturas:
        print(fatura)

    conn.close()


