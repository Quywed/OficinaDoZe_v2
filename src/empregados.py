import sqlite3

def listar_empregados(conn):
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


