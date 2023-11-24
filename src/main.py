from clientes import *
from faturas import *
from veiculos import *
import hashlib

####################################################################
#
# TODO: CRIAR FUNCOES DE CRUD PARA CADA TABELA 
#       IMPORT DAS DEVIDAS FUNCOES
# TODO: ADICIONAR SISTEMA DE LOGIN
#
# ...
#
#
#
####################################################################

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def login(cursor, letra):
    # INPUTS
    nif_input = input("|LOGIN|\n NIF: ")
    password_input = input("Password: ")

    hashed_password_input = hash_password(password_input)

    if letra == 'c':
        # CHECK CLIENT
        cursor.execute("SELECT * FROM clientes WHERE nif = ? AND password_hash = ?", (nif_input, hashed_password_input))
        client = cursor.fetchall()

        if client:        
            
            
            return True
        else:
            print("Cliente não foi encontrado ou introduziu a senha incorretamente.")
            return False

    elif letra == 'e':
        # CHECK empregado
        cursor.execute("SELECT * FROM empregados WHERE empregado_nif = ? AND password_hash = ?", (nif_input, hashed_password_input))
        empregado = cursor.fetchall()
 
        if empregado:



            return True
        else:
            print("Empregado não foi encontrado ou introduziu a senha incorretamente.")
            return False


def menu():
    """Menu principal da aplicação"""

    # CONEXAO
    conn = sqlite3.connect('src/oficina.db')

    # CURSOR PARA EXECUTAR QUERYS
    cursor = conn.cursor()
    while True:
        print("""
            *********************************************************************
            :                (-: OFICINA DO ZÉ - MORTE AO IUC :-)               :
            *********************************************************************
            : LOGIN                                                             :
            :                           C - Cliente                             :
            :                           E - Empregado                           :
            :                                                                   :
            :                                                                   :
            :                                                                   :
            : X - EXIT                                                          :
            :                                                                   :
            *********************************************************************
            """)

        op = input("opcao?")
        if op == 'c':
            #cliente_encontrado = login(conn, op) | este valor deve ser o nif do cliente encontrado
            # Entrar em Login Clientes  
            print("""
            *********************************************************************
            :                (-: OFICINA DO ZÉ - MORTE AO IUC :-)               :
            *********************************************************************
            : LOGIN CLIENTES                                                    :
            :                           L - Login                               :
            :                           C - Criar Conta                         :
            :                                                                   :
            :                                                                   :
            :                                                                   :
            : X - EXIT                                                          :
            :                                                                   :
            *********************************************************************
            """)
            if op == 'l':
                # TODO Login Clientes
                
                pass
            elif op == 'c':
                # TODO Criar Conta Clientes
                pass

        elif op == 'e':
            # Entrar em Empregados
            #cliente_encontrado = login(conn, op) | este valor deve ser um boolean, se for true apresenta as funcoes. senao, baza
            # TODO Inserir funçao para login empregados
            pass


        elif op == "x":
            exit()
    
        while True:
            print("""
            *********************************************************************
            :                (-: OFICINA DO ZÉ - MORTE AO IUC :-)               :
            *********************************************************************
            :                                                                   :
            :                           C - Cliente                             :
            :                           V - Veiculo                             :
            :                           F - Fatura                              :
            :                                                                   :
            :                                                                   :
            : X - EXIT                                                          :
            :                                                                   :
            *********************************************************************
            """)

            op = input("opcao?")

            if op == "x":
                exit()
            
    #CRIACAO
            elif op == "c":
                #TODO FUNCAO CRIAR CLIENTE
                print("""
                        *********************************************************************
                        :                (-: OFICINA DO ZÉ - MORTE AO IUC :-)               :
                        *********************************************************************
                        : CLIENTES                                                          :
                        :                       1 - Inserir Novo Cliente                    :
                        :                       2 - Listar Todos os Clientes                :
                        :                                                                   :
                        :                                                                   :
                        :                                                                   :
                        : X - EXIT                                                          :
                        :                                                                   :
                        *********************************************************************
                        """)

                op = input("opcao?")
                if op == "1":
                    #TODO FUNCAO INSERIR NOVO CLIENTE
                    inserir_novo_cliente(conn)
                elif op == "2":
                    #TODO FUNCAO LISTAR TODOS OS CLIENTES    
                    imprime_lista_de_clientes(conn)
                elif op == "x":
                    exit()

            elif op == "v":
                #TODO FUNCAO CRIAR VEICULO
                print("""
                        *********************************************************************
                        :                (-: OFICINA DO ZÉ - MORTE AO IUC :-)               :
                        *********************************************************************
                        : VEICULOS                                                          :
                        :                       1 - Inserir Veiculos                        :
                        :                       2 - Listar Veiculos de um Cliente           :
                        :                       3 - Listar Todos os Veiculos                :
                        :                                                                   :
                        :                                                                   :
                        : X - EXIT                                                          :
                        :                                                                   :
                        *********************************************************************
                        """)

                op = input("opcao?")
                if op == "1":
                    #TODO FUNCAO INSERIR VEICULO
                    insert_veiculo(conn)
                elif op == "2":
                    #TODO FUNCAO LISTAR VEICULOS DE UM CLIENTE
                    cliente_nif = input("Insira o NIF do Cliente: " )
                    select_veiculo_cliente(conn, cliente_nif)
                elif op == "3":
                    #TODO FUNCAO LISTAR TODOS OS VEICULOS
                    list_veiculos(conn)
                elif op == "x":
                    exit()
        
            elif op == "f":
                #TODO FUNCAO CRIAR FATURA
                print("""
                        *********************************************************************
                        :                (-: OFICINA DO ZÉ - MORTE AO IUC :-)               :
                        *********************************************************************
                        : FATURAS                                                           :
                        :                       1 - Criar Nova Fatura                       :
                        :                       2 - Listar Faturas De um CLiente            :
                        :                       3 - Listar Todas as Faturas                 :
                        :                                                                   :
                        :                                                                   :
                        : X - EXIT                                                          :
                        :                                                                   :
                        *********************************************************************
                        """)

                op = input("opcao?")
                if op == "1":
                    #TODO FUNCAO INSERIR FATURA
                    cria_nova_fatura(conn)
                elif op == "2":
                    #TODO FUNCAO LISTAR FATURA DE UM CLIENTE
                    cliente_nif = input("Insira o NIF do Cliente: " )
                    faturas_cliente(conn,cliente_nif)
                elif op == "3":
                    #TODO FUNCAO LISTAR TODOS AS FATURAS
                    imprime_lista_de_faturas(conn)
                elif op == "x":
                    exit()
    

if __name__ == "__main__":
    menu()
