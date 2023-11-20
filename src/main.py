from clientes import *
#from faturas import 
#from io_ficheiros import (carrega_as_listas_dos_ficheiros, guarda_as_listas_em_ficheiros)
#from io_terminal import pause
from veiculos import *



####################################################################
#
# TODO: CRIAR FUNCOES DE CRUD PARA CADA TABELA 
#       IMPORT DAS DEVIDAS FUNCOES
#
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
        :    (-: OFICINA DO ZÉ - MORTE AO IUC :-)                           :
        *********************************************************************
        :                                                                   :
        : CC - CRIAR Cliente         LC - LISTAR Clientes                   :
        : CV - CRIAR Veiculo         LV - LISTAR Veiculos                   :
        : CF - CRIAR Fatura          LF - LISTAR Faturas                    :
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
        elif op == "cc":
            #TODO FUNCAO CRIAR CLIENTE
            pass

        elif op == "cv":
            #TODO FUNCAO CRIAR VEICULO
            insert_veiculo(conn)

        elif op == "cf":
            #TODO FUNCAO CRIAR FATURA
            pass

#LISTAGEM
        elif op == "lc":
           #TODO FUNCAO LISTAR CLIENTES
           imprime_lista_de_clientes(conn)
           pass

        elif op == "lv":
            list_veiculos(conn)
            #TODO FUNCAO LISTAR VEICULOS
            pass

        elif op == "lf":
            #TODO FUNCAO LISTAR FATURAS
            pass

if __name__ == "__main__":
    menu()
