import sqlite3
from datetime import datetime
import random
import hashlib

def hash_password(password):
    """
    Retorna o hash SHA-256 da senha fornecida.

    :param password: A senha a ser criptografada.
    :type password: str
    :return: O hash SHA-256 da senha.
    :rtype: str
    """
    return hashlib.sha256(password.encode()).hexdigest()

def creates_bd(conn):
    """Cria as tabelas na base de dados.

    Esta função cria as tabelas na base de dados SQLite 'oficina.db' localizada no diretório 'src'.
    As tabelas criadas são Veiculos, clientes, empregados e faturas se elas ainda não existirem.

    Args:
        conn: Objeto de conexão com a base de dados.

    Raises:
        OperationalError: Se ocorrer um erro ao criar as tabelas.

    Returns:
        None
    """
    # CONEXAO
    conn = sqlite3.connect('src/oficina.db')

    # CURSOR PARA EXECUTAR QUERYS
    cursor = conn.cursor()

    # TABELA Veiculos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Veiculos (
            matricula TEXT PRIMARY KEY,
            modelo TEXT,
            marca TEXT,
            ano INTEGER,
            km INTEGER,
            nome_motor TEXT,
            cliente_nif INTEGER,
            FOREIGN KEY (cliente_nif) REFERENCES clientes(nif)
        );
    ''')

    # TABELA clientes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            nif INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            telefone TEXT,
            password_hash TEXT
        );
    ''')

    # TABELA empregados
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empregados (
            empregado_nif INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            password_hash TEXT
        );
    ''')

    # TABELA faturas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS faturas (
            id INTEGER PRIMARY KEY,
            cliente_nif INTEGER,
            data_criacao DATE DEFAULT CURRENT_DATE,
            descricao TEXT,
            valor REAL,
            FOREIGN KEY (cliente_nif) REFERENCES clientes(nif)
        );
        ''')
    conn.commit()  # COMMIT

conn = sqlite3.connect('src/oficina.db')
creates_bd(conn)


#-----------------------------------INSERTS RANDOM-----------------------------------------------
def inserts_random(conn):
    """Insere dados aleatórios nas tabelas.

    Esta função insere dados fictícios nas tabelas Veiculos, clientes e faturas na base de dados SQLite
    utilizando uma conexão fornecida.

    Args:
        conn: Objeto de conexão com a base de dados.

    Returns:
        None
    """

    veiculos_data = []
    clientes_data = []
    empregados_data = []
    faturas_data = []
    cursor = conn.cursor()

    cliente_random_1 = random.randint(1000, 9999)
    cliente_random_2 = random.randint(1000, 9999)

    empregado_random_1 = random.randint(1000, 9999)
    empregado_random_2 = random.randint(1000, 9999)
    list_nif_empregado = [empregado_random_1, empregado_random_2]

    #INSERT EMPREGADOS-----------------------------------------------
    #INSERT EMPREGADOS-----------------------------------------------
    for e in range(2):
        password_empregado = "password_empregado" 
        password_hash_empregado = hashlib.sha256(password_empregado.encode()).hexdigest()
        empregados_data.append((list_nif_empregado[e], f'Empregado{e}', f'empregado{e}@email.com', password_hash_empregado))

    cursor.executemany("INSERT INTO empregados VALUES (?, ?, ?, ?)", empregados_data)
    #---------------------------------------------------------------

    #INSERT CLIENTES-----------------------------------------------
    password_cliente = "password_cliente"
    password_hash_cliente = hashlib.sha256(password_cliente.encode()).hexdigest()

    #CLIENTE 1
    password_hash_cliente = hashlib.sha256(password_cliente.encode()).hexdigest()
    clientes_data.append((cliente_random_1,'Cliente1', 'cliente1@email.com', '123456789', password_hash_cliente))

    #CLIENTE 2 
    password_hash_cliente = hashlib.sha256(password_cliente.encode()).hexdigest()
    clientes_data.append((cliente_random_2,'Cliente2', 'cliente2@email.com', '987654321', password_hash_cliente))

    #--------------------------------------------------------------
    #INSERT MATRICULAS---------------------------------------------
    num_random_1 = random.randint(100, 999)
    num_random_2 = random.randint(100, 999)

    matricula_random_1 = "ABC_" + str(num_random_1)
    matricula_random_2 = "CBA_" + str(num_random_2)

    #MATRICULA 1
    veiculos_data.append((matricula_random_1, 'Modelo1', 'Marca1', 2020, 50000, 'Motor1', cliente_random_1))

    #MATRICULA 2
    veiculos_data.append((matricula_random_2, 'Modelo2', 'Marca2', 2020, 50000, 'Motor2', cliente_random_2))

    #--------------------------------------------------------------
    #INSERT FATURAS------------------------------------------------

    faturas_random_1 = random.randint(100, 999)
    faturas_random_2 = random.randint(100, 999)

    #FATURA 1
    faturas_data.append((faturas_random_1, cliente_random_1, datetime.now(), 'Servico1', 100.00))

    #FATURA 2
    faturas_data.append((faturas_random_2, cliente_random_2, datetime.now(), 'Servico2', 200.00))

    cursor.executemany("INSERT INTO Veiculos VALUES (?, ?, ?, ?, ?, ?, ?)", veiculos_data)
    cursor.executemany("INSERT INTO clientes VALUES (?, ?, ?, ?, ?)", clientes_data)
    cursor.executemany("INSERT INTO faturas VALUES (?, ?, ?, ?, ?)", faturas_data)

    conn.commit()  # COMMIT

conn = sqlite3.connect('src/oficina.db')
inserts_random(conn)


def listar_tabelas(conn):
    """Lista o conteúdo das tabelas na base de dados.

    Esta função realiza uma seleção de todos os registros em cada tabela
    (Veiculos, clientes, empregados, faturas) na base de dados e exibe
    o conteúdo de cada uma.

    Args:
        conn: Objeto de conexão com a base de dados.

    Returns:
        None
    """

    cursor = conn.cursor()

    # LISTAR (SELECT)
    cursor.execute("SELECT * FROM Veiculos;")
    veiculos = cursor.fetchall()

    print("\nVEICULOS:")
    for veiculo in veiculos:
        print(veiculo)

    cursor.execute("SELECT * FROM clientes;")
    clientes = cursor.fetchall()

    print("\nCLIENTES:")
    for cliente in clientes:
        print(cliente)

    cursor.execute("SELECT * FROM empregados;")
    empregados = cursor.fetchall()

    print("\nEMPREGADO:")
    for i in empregados:
        print(i)

    cursor.execute("SELECT * FROM faturas;")
    faturas = cursor.fetchall()

    print("\nFATURAS:")
    for fatura in faturas:
        print(fatura)

    conn.commit()  # COMMIT
    conn.close()   # FECHAR A CONEXAO

conn = sqlite3.connect('src/oficina.db')
listar_tabelas(conn)