from clientes import *
from faturas import *
from veiculos import *
from empregados import *
import hashlib
import getpass


def cliente(conn, logged_user):

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
    return hashlib.sha256(password.encode()).hexdigest()


def login(cursor, letra):
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
    while True:
        """Menu principal da aplicação"""
        # CONEXAO
        conn = sqlite3.connect('src/oficina.db')

        # CURSOR PARA EXECUTAR QUERYS
        cursor = conn.cursor()

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


            
