from clientes import *
from faturas import *
#from io_ficheiros import (carrega_as_listas_dos_ficheiros, guarda_as_listas_em_ficheiros)
#from io_terminal import pause
from veiculos import *



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
