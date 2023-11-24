import sqlite3
import hashlib

# CONEXAO
conn = sqlite3.connect('src/oficina.db')
cursor = conn.cursor()

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
            
            
            return str(nif_input)
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






#MAIN DO TESTE
choice = input("Opção: (c - cliente | e - empregado)")


if choice == 'c':
    cursor.execute("SELECT * FROM clientes;")
    clientes = cursor.fetchall()

    print("\nCLIENTES:")
    for cliente in clientes:
        print(cliente)

    cliente_encontrado = login(cursor, choice)
    if cliente_encontrado != "":
        print ('funcões do cliente')

elif choice == 'e':
    cursor.execute("SELECT * FROM empregados;")
    empregados = cursor.fetchall()

    print("\nCLIENTES:")
    for empregado in empregados:
        print(empregado)


    empregado_encontrado = login(cursor, choice)
    if empregado_encontrado == True:
        print('funções do empregado')


    