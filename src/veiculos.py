import sqlite3  

def insert_veiculo(conn):

    cursor = conn.cursor()
    matricula = input("Matricula: ")
    modelo = input("Modelo: ")
    marca = input("Marca: ")
    ano = int(input("Ano: "))
    km = int(input("Km: "))
    nome_motor = input("Nome do Motor: ")
    cliente_nif = int(input("NIF Cliente: "))


    try:
        cursor.execute('''
            INSERT INTO Veiculos (matricula, modelo, marca, ano, km, nome_motor, cliente_nif)
            VALUES (?, ?, ?, ?, ?, ?, ?);
        ''', (matricula, modelo, marca, ano, km, nome_motor, cliente_nif))

        conn.commit()
        print("Veiculo inserido com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro no insert do veiculo: {e}")
        conn.rollback()

    conn = sqlite3.connect('src/oficina.db')
    conn.close()



def select_veiculo_cliente(conn, client_nif):
    try:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM Veiculos WHERE cliente_nif = ?;
        ''', (client_nif,))

        cars = cursor.fetchall()

        if cars:
            print(f"Carros do Cliente com o NIF:{client_nif}:")
            for car in cars:
                print(f"Matricula: {car[0]}, Modelo: {car[1]}, Marca: {car[2]}, Ano: {car[3]}, KM: {car[4]}, Nome do Motor: {car[5]}")
        else:
            print(f"O Cliente com o NIF: {client_nif} não tem carros")

    except sqlite3.Error as e:
        print(f"Erro ao procurar os carros: {e}")


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

    except sqlite3.Error as e:
        print(f"Erro: {e}")


