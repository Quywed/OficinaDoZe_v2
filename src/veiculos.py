import sqlite3  

def insert_veiculo(conn):
    """
    Insere um veículo na tabela 'Veiculos' da base de dados.

    :param conn: Conexão ativa com o base de dados SQLite.
    :type conn: sqlite3.Connection
    :raises ValueError: Se o ano estiver fora do intervalo válido (1900-2023)
                        ou se a quilometragem for negativa.
    """

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

    finally:
        conn.close()



def select_veiculo_cliente(conn, client_nif):
    """
    Seleciona os veículos de um cliente específico da tabela 'Veiculos'.

    :param conn: Conexão ativa com a base de dados SQLite.
    :type conn: sqlite3.Connection
    :param client_nif: NIF do cliente para o qual os veículos serão selecionados.
    :type client_nif: int
    """
    
    try:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM Veiculos WHERE cliente_nif = ?;
        ''', (client_nif,))

        cars = cursor.fetchall()

        if cars:
            print(f"Carros do Cliente com o NIF: {client_nif}:")
            for car in cars:
                print(f"Matricula: {car[0]}, Modelo: {car[1]}, Marca: {car[2]}, Ano: {car[3]}, KM: {car[4]}, Nome do Motor: {car[5]}")
        else:
            print(f"O Cliente com o NIF: {client_nif} não tem carros")

    except sqlite3.Error as sqlite_error:
        print(f"Erro no SQLite durante a execução da query: {sqlite_error}")

    except Exception as e:
        print(f"Erro inesperado: {e}")

    finally:
        conn.close()


def list_veiculos(conn):
    """
    Lista todos os veículos presentes na tabela 'Veiculos' da base de dados.

    :param conn: Conexão ativa com a base de dados SQLite.
    :type conn: sqlite3.Connection
    """
    
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

    finally:
        conn.close()

