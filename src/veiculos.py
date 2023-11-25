import sqlite3  

def insert_veiculo(conn):
    try:
        cursor = conn.cursor()

        matricula = input("Matricula: ")
        modelo = input("Modelo: ")
        marca = input("Marca: ")
        ano = int(input("Ano:  "))
        km = int(input("Km: "))
        nome_motor = input("Nome do Motor: ")
        cliente_nif = int(input("NIF Cliente: "))

        if ano < 1900 or ano > 2023:
            raise ValueError("Ano inválido. Deve estar entre 1900 e 2023.")

        if km < 0:
            raise ValueError("A quilometragem não pode ser negativa.")

        cursor.execute('''
            INSERT INTO Veiculos (matricula, modelo, marca, ano, km, nome_motor, cliente_nif)
            VALUES (?, ?, ?, ?, ?, ?, ?);
        ''', (matricula, modelo, marca, ano, km, nome_motor, cliente_nif))

        conn.commit()
        print("Veiculo inserido com sucesso.")

    except sqlite3.Error as sqlite_error:
        print(f"Erro no SQLite durante a execução da query: {sqlite_error}")
        conn.rollback()

    except ValueError as value_error:
        print(f"Erro nos dados inseridos: {value_error}")
        conn.rollback()

    except Exception as e:
        print(f"Erro inesperado: {e}")
        conn.rollback()

    



def select_veiculo_cliente(conn, client_nif):
    try:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM Veiculos WHERE cliente_nif = ?;
        ''', (client_nif,))

        carros = cursor.fetchall()

        if carros:
            print(f"\ncarroros do Cliente com o NIF: {client_nif}:")

            # Print header
            print(f"{'Matricula': <15}" + " | " + f"{'Modelo': <20}" + " | " + f"{'Marca': <15}" + " | " +
                  f"{'Ano': <5}" + " | " + f"{'KM': <8}" + " | " + f"{'Nome do Motor': <20}\n")

            
            for carro in carros:
                print(f"{carro[0]: <15}" + " | " + f"{carro[1]: <20}" + " | " + f"{carro[2]: <15}" + " | " +
                      f"{carro[3]: <5}" + " | " + f"{carro[4]: <8}" + " | " + f"{carro[5]: <20}")
        else:
            print(f"O Cliente com o NIF: {client_nif} não tem carroros")

    except sqlite3.Error as sqlite_error:
        print(f"Erro no SQLite durante a execução da query: {sqlite_error}")

    except Exception as e:
        print(f"Erro inesperado: {e}")



def list_veiculos(conn):
    try:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM Veiculos;
        ''')

        veiculos = cursor.fetchall()

        if veiculos:
            print("Todos os Veiculos:")
            for veiculo in veiculos:
                print(f"Matricula: {veiculo[0]}, Modelo: {veiculo[1]}, Marca: {veiculo[2]}, Ano: {veiculo[3]}, KM: {veiculo[4]}, Nome do Motor: {veiculo[5]}, Cliente NIF: {veiculo[6]}")
        else:
            print("Não ouve veiculos encontrados na Tabela")

    except sqlite3.Error as sqlite_error:
        print(f"Erro no SQLite durante a execução da query: {sqlite_error}")

    except Exception as e:
        print(f"Erro inesperado: {e}")
