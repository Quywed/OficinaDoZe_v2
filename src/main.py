from clientes import *
from faturas import *
from veiculos import *
from empregados import *
import hashlib
import getpass


def cliente(conn, logged_user):
    """Interface para acesso do cliente às informações.

    Esta função representa uma interface de usuário para clientes acessarem informações relacionadas às suas contas
    na oficina. Ela permite que o cliente visualize seus dados pessoais, veículos e faturas, bem como oferece a opção
    de sair da interface.

    Args:
        conn: Objeto de conexão com a base de dados.
        logged_user: Dados do usuário logado (cliente) atualmente na interface.

    Returns:
        None
    """
    while True: 
        print("""
    *********************************************************************
    :                (-: OFICINA DO ZÉ - MORTE AO IUC :-)               :
    *********************************************************************
    : LOGIN CLIENTES                                                    :
    :                           1 - Ver os Meus Dados                   :
    :                           2 - Ver os Meus Veiculos                :
    :                           3 - Ver as Minhas Faturas               :
    :                                                                   :
    :                                                                   :
    :  X -EXIT                                                          :
    :                                                                   :
    *********************************************************************
    """)
        opc = input("opcao?")
        if opc == '1':
            # Ver os Meus Dados
            client_nif = str(logged_user['id'])
            select_informacao_cliente(conn, client_nif)
            pass
        elif opc == '2':
            # Ver os Meus Veiculos
            client_nif = str(logged_user['id'])
            select_veiculo_cliente(conn, client_nif)
        elif opc == "3":
            # Ver as Minhas Faturas
            client_nif = str(logged_user['id'])
            faturas_cliente(conn, client_nif)
        elif opc == "R" or opc == "r":
            logged_user = None
        elif opc == "x":
            exit()


def empregado(conn):
    """Interface para acesso às opções dos funcionários na oficina.

    Esta função representa uma interface de usuário para funcionários da oficina. 
    Permite que eles acessem diferentes seções do sistema, como clientes, veículos e faturas, 
    fornecendo opções específicas dentro de cada seção.

    Args:
        conn: Objeto de conexão com a base de dados.

    Returns:
        None
    """
    
    while True:
        print("""
    *********************************************************************
    :                (-: OFICINA DO ZÉ - MORTE AO IUC :-)               :
    *********************************************************************
    : MENU EMPREGADOS                                                   :
    :                                                                   :
    :                                                                   :
    :                            1 - CLIENTES                           :
    :                            2 - VEICULOS                           :
    :                            3 - FATURAS                            :                                                                  
    :                                                                   :
    :                                                                   :
    :                                                                   :
    : X - EXIT                                                          :
    :                                                                   :
    *********************************************************************
    """)
        ope = input("opcao?")
        if ope == "1":
            print("""
        *********************************************************************
        :                (-: OFICINA DO ZÉ - MORTE AO IUC :-)               :
        *********************************************************************
        : MENU EMPREGADOS                                                   :
        :                                                                   :
        :                                                                   :
        :                       1 - Inserir Novo Cliente                    :
        :                       2 - Listar Todos os Clientes                :
        :                                                                   :                                                                  
        :                                                                   :
        :                                                                   :
        :X - EXIT                                                           :
        :                                                                   :
        *********************************************************************
        """)
            opo = input("opcao?")
            if opo == "1":

                inserir_novo_cliente(conn)
            elif opo == "2":

                imprime_lista_de_clientes(conn)
  
            elif opo == "x":
                exit()

        elif ope == "2":
            print("""
            *********************************************************************
            :                (-: OFICINA DO ZÉ - MORTE AO IUC :-)               :
            *********************************************************************
            : MENU EMPREGADOS                                                   :
            :                                                                   :
            :                                                                   :
            :                   1 - Inserir novo Veiculo                        :
            :                   2 - Listar Veiculo de um Cliente                :
            :                   3 - Listar todos os Veiculo                     :                                                                  
            :                                                                   :
            :                                                                   :
            :X -EXIT                                                            :
            :                                                                   :
            *********************************************************************
            """)
            opo = input("opcao?")
            if opo == "1":

                insert_veiculo(conn)
            elif opo == "2":

                client_nif = input("NIF do CLiente: ")
                select_veiculo_cliente(conn, client_nif)
            elif opo == "3":

                list_veiculos(conn)

            elif opo == "x":
                exit()

        elif ope == "3":
            print("""
            *********************************************************************
            :                (-: OFICINA DO ZÉ - MORTE AO IUC :-)               :
            *********************************************************************
            : MENU EMPREGADOS                                                   :
            :                                                                   :
            :                                                                   :
            :                    1 - Criar um Nova Fatura                       :
            :                    2 - Listar Todas as Faturas                    :
            :                    3 - Listar Faturas de um Cliente               :                                                                  
            :                                                                   :
            :                                                                   :
            : X - EXIT                                                          :
            :                                                                   :
            *********************************************************************
            """)
            opo = input("opcao?")
            if opo == "1":

                cria_nova_fatura(conn)
            elif opo == "2":

                imprime_lista_de_faturas(conn)
            elif opo == "3":

                client_nif = input("NIF do CLiente: ")
                faturas_cliente(conn, client_nif)
                

            elif opo == "R" or opo == "r":
                pass

            elif opo == "x":
                exit()      

        elif ope == "x":
            exit()

def hash_password(password):
    """Cria um hash SHA256 da senha fornecida.

    Args:
        password (str): Senha a ser convertida em hash.

    Returns:
        str: Hash SHA256 da senha.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def login(cursor, letra):
    """Realiza o login de clientes ou empregados no sistema.

    Esta função permite que clientes (letra 'c') e empregados (letra 'e') façam login no sistema,
    verificando as credenciais fornecidas no banco de dados.

    Args:
        cursor: Cursor para executar consultas no banco de dados.
        letra (str): Letra identificadora ('c' para cliente, 'e' para empregado).

    Returns:
        dict or False: Um dicionário com informações de autenticação se o login for bem-sucedido.
            O dicionário contém 'type' (tipo: 'client' ou 'employee') e 'id' (identificação).
            Retorna False se o login falhar.
    """
    # INPUTS
    nif_input = input("|LOGIN|\n NIF: ")
    password_input = getpass.getpass("Password: ")

    hashed_password_input = hash_password(password_input)

    if letra == 'c':
        # CHECK CLIENT
        cursor.execute("SELECT * FROM clientes WHERE nif = ? AND password_hash = ?", (nif_input, hashed_password_input))
        client = cursor.fetchall()

        if client:        
            return {'type': 'client', 'id': str(nif_input)}
        else:
            print("Cliente não foi encontrado ou introduziu a senha incorretamente.")
            exit()

    elif letra == 'e':
        # CHECK empregado
        cursor.execute("SELECT * FROM empregados WHERE empregado_nif = ? AND password_hash = ?", (nif_input, hashed_password_input))
        empregado = cursor.fetchall()
 
        if empregado:
            return {'type': 'employee', 'id': str(nif_input)}
        else:
            print("Empregado não foi encontrado ou introduziu a senha incorretamente.")
            return False

def menu():
    """Exibe o menu principal da aplicação e direciona para os submenus de login de clientes e empregados.

    O menu principal permite escolher entre realizar login como cliente ou empregado,
    redirecionando para os menus correspondentes.

    As opções disponíveis:
    1. Cliente: Redireciona para o submenu de login ou criação de conta para clientes.
    2. Empregado: Realiza o login como empregado.
    X: Sai da aplicação.

    """

    # CONEXAO
    conn = sqlite3.connect('src/oficina.db')

    # CURSOR PARA EXECUTAR QUERYS
    cursor = conn.cursor()

    while True:
        """Menu principal da aplicação"""
        

        logged_user = None
        print("""
            *********************************************************************
            :                (-: OFICINA DO ZÉ - MORTE AO IUC :-)               :
            *********************************************************************
            : LOGIN                                                             :
            :                           1 - Cliente                             :
            :                           2 - Empregado                           :
            :                                                                   :
            :                                                                   :
            :                                                                   :
            :  X - EXIT                                                         :
            :                                                                   :
            *********************************************************************
            """)

        op = input("opcao?")
        if op == "1":
            # Entrar em Login Clientes  
            print("""
            *********************************************************************
            :                (-: OFICINA DO ZÉ - MORTE AO IUC :-)               :
            *********************************************************************
            : LOGIN CLIENTES                                                    :
            :                           c - Login                               :
            :                           cc - Criar Conta                        :
            :                                                                   :
            :                                                                   :
            :                                                                   :
            : X - EXIT                                                          :
            :                                                                   :
            *********************************************************************
            """)
            opc = input("opcao?")
            if opc == 'c':
                # Login Clientes
                logged_user = login(cursor, opc)
                if logged_user and logged_user['type'] == 'client':
                    cliente(conn,logged_user)
                else:
                    print("Login falhou. Cliente não encontrado ou senha incorreta.")
            if opc == 'cc':
                inserir_novo_cliente(conn)
        
        elif op == '2':
            # Entrar em Empregados
            empregado_encontrado = login(cursor, op)
            if empregado_encontrado != False:
                empregado(conn)
        elif op == 'x':
            exit()


if __name__ == "__main__":
    menu()


            
