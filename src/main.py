from clientes import cria_novo_cliente, imprime_lista_de_clientes
#from faturas import 
#from io_ficheiros import (carrega_as_listas_dos_ficheiros, guarda_as_listas_em_ficheiros)
#from io_terminal import pause
from veiculos import insert_veiculo, list_veiculo



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
    
    lista_de_veiculos = []
    lista_de_clientes = []
    lista_de_faturas = []

    while True:
        print("""
        *********************************************************************
        :    (-: OFICINA BARATINHA - RESISTIMOS A QUALQUER ORÇAMENTO :-)    :
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

        op = input("opcao?").lower()

        if op == "x":
            exit()

#CRIACAO
        elif op == "CC":
            #TODO FUNCAO CRIAR CLIENTE
            continue

        elif op == "CV":
            #TODO FUNCAO CRIAR VEICULO
            insert_veiculo(conn)

        elif op == "CF":
            #TODO FUNCAO CRIAR FATURA
            continue

#LISTAGEM
        elif op == "LC":
           #TODO FUNCAO LISTAR CLIENTES
           pass

        elif op == "LV":
            list_veiculos(conn)
            #TODO FUNCAO LISTAR VEICULOS
            pass

        elif op == "LF":
            #TODO FUNCAO LISTAR FATURAS
            pass

if __name__ == "__main__":
    menu()
