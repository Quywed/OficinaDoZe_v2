import sqlite3
import getpass
import hashlib

def inserir_novo_empregado(conn):
    """
    Insere um novo empregado na base de dados.

    :param conn: Conexão à base de dados.
    :type conn: sqlite3.Connection
    """

    try:
        empregados_data = []


        cursor = conn.cursor()
        cursor.execute("SELECT * FROM empregados;")
        empregados = cursor.fetchall()

        print("\nEMPREGADOS:")
        for empregado in empregados:
            print(empregado)

        nome = input("EMPREGADO\nNome: ")
        nif = input("NIF: ")
        email = input("Email: ")
        password = getpass.getpass("Password: ")

        password_hash_empregado = hashlib.sha256(password.encode()).hexdigest()
                              # NIF               NOME          EMAIL          PASSWORD
        empregados_data.append((nif, nome, email, password_hash_empregado))

        cursor.executemany("INSERT INTO empregados VALUES (?, ?, ?, ?)", empregados_data)

    except sqlite3.IntegrityError as e:
        print("Ocorreu um erro. O empregado com o NIF: '" + nif + "' já deve existir na BD.")
    
    conn.commit()


def listar_empregados(conn):
    """
    Lista todos os empregados na base de dados.

    :param conn: Conexão à base de dados.
    :type conn: sqlite3.Connection
    """

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM empregados')
    registros = cursor.fetchall()

    conn.close()

    if registros:

        print("{:<15} {:<30} {:<30}".format("NIF", "Nome", "Email"))
        print("="*110)  


        for registro in registros:
            nif, nome, email = registro
            print("{:<15} {:<30} {:<30}".format(nif, nome, email))
    else:
        print("Nenhum registro encontrado na tabela empregados.")

def select_informacao_empregado(conn, empregado_nif):
    """
    Seleciona e exibe as informações de um empregado com base no NIF.

    :param conn: Conexão à base de dados.
    :type conn: sqlite3.Connection
    :param empregado_nif: NIF do empregado a ser consultado.
    :type empregado_nif: str
    """

    try:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM empregados WHERE empregado_nif = ?;
        ''', (empregado_nif,))

        empregado_info = cursor.fetchone()

        if empregado_info:
            print("\nInformação do Empregado:")
            print(f"NIF: {empregado_info[0]}")
            print(f"Nome: {empregado_info[1]}")
            print(f"Email: {empregado_info[2]}")

           
        else:
            print(f"Empregado com NIF {empregado_nif} não encontrado.")

    except sqlite3.Error as e:
        print(f"Erro: {e}")




