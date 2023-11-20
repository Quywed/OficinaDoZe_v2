from io_terminal import imprime_lista

nome_ficheiro_lista_de_clientes = "lista_de_clientes.pk"

def imprime_lista_de_clientes(lista_de_clientes):
    """TODO: documentação"""

    #TODO: Implementar esta função
    # ...

def cria_novo_cliente():
    # Inicialize um dicionário vazio para armazenar as informações do cliente
    novo_cliente = {}

    # Solicite as informações do cliente ao usuário
    novo_cliente["nome"] = input("Nome do cliente: ")
    novo_cliente["nif"] = input("NIF do cliente: ")
    novo_cliente["email"] = input("E-mail do cliente: ")
    novo_cliente["telefone"] = input("Telefone do cliente: ")

    # Retorne o dicionário com as informações do novo cliente
    return novo_cliente

nome_ficheiro_lista_de_clientes = "lista_de_clientes.pk"

def imprime_lista_de_clientes(lista_de_clientes):
    """
    Imprime a lista de clientes.

    :param lista_de_clientes: Uma lista de dicionários, onde cada dicionário contém informações de um cliente.
    """
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

