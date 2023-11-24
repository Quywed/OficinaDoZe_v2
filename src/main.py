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
            
            
            return nif_input
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
            :                           1 - Cliente                             :
            :                           2 - Empregado                           :
            :                                                                   :
            :                                                                   :
            :                                                                   :
            : X - EXIT                                                          :
            :                                                                   :
            *********************************************************************
            """)

        op = input("opcao?")
        if op == "1":
            #cliente_encontrado = login(conn, op) | este valor deve ser o nif do cliente encontrado
            # Entrar em Login Clientes  
            print("""
            *********************************************************************
            :                (-: OFICINA DO ZÉ - MORTE AO IUC :-)               :
            *********************************************************************
            : LOGIN CLIENTES                                                    :
            :                           C - Login                               :
            :                           CC - Criar Conta                         :
            :                                                                   :
            :                                                                   :
            :                                                                   :
            : X - EXIT                                                          :
            :                                                                   :
            *********************************************************************
            """)
            opc = input("opcao?")
            if opc == 'c':
                # TODO Login Clientes | As funcoes teem que ser adicionadas apenas usando o cliente encontrado
                cliente_encontrado = login(cursor,opc)
                if cliente_encontrado != "":
                    print("Nif do gajo " + str(cliente_encontrado))

                pass
            elif opc == 'cc':
                # TODO Criar Conta Clientes
                pass

        elif op == 'e':
            # Entrar em Empregados
            #cliente_encontrado = login(conn, op) | este valor deve ser um boolean, se for true apresenta as funcoes. senao, baza
            # TODO Inserir funçao para login empregados
            pass


        elif op == "x":
            exit()
    

if __name__ == "__main__":
    menu()
