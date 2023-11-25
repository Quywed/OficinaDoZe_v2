import sqlite3
from datetime import datetime
import random
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

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

#-----------------------------------INSERTS RANDOM-----------------------------------------------

veiculos_data = []
clientes_data = []
empregados_data = []
faturas_data = []

cliente_random_1 = random.randint(1000, 9999)
cliente_random_2 = random.randint(1000, 9999)

#INSERT EMPREGADOS-----------------------------------------------
#INSERT EMPREGADOS-----------------------------------------------
for e in range(2):
    password_empregado = "password_empregado" 
    password_hash_empregado = hashlib.sha256(password_empregado.encode()).hexdigest()
    empregados_data.append((e + 1, f'Empregado{e}', f'empregado{e}@email.com', password_hash_empregado))

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
matricula_random_1 = "ABC_200"
matricula_random_2 = "CBA_300"

#MATRICULA 1
veiculos_data.append((matricula_random_1, 'Modelo1', 'Marca1', 2020, 50000, 'Motor1', cliente_random_1))

#MATRICULA 2
veiculos_data.append((matricula_random_2, 'Modelo2', 'Marca2', 2020, 50000, 'Motor2', cliente_random_2))

#--------------------------------------------------------------
#INSERT FATURAS------------------------------------------------

faturas_random_1 = 111
faturas_random_2 = 222

#FATURA 1
faturas_data.append((faturas_random_1, cliente_random_1, datetime.now(), 'Servico1', 100.00))

#FATURA 2
faturas_data.append((faturas_random_2, cliente_random_2, datetime.now(), 'Servico2', 200.00))

cursor.executemany("INSERT INTO Veiculos VALUES (?, ?, ?, ?, ?, ?, ?)", veiculos_data)
cursor.executemany("INSERT INTO clientes VALUES (?, ?, ?, ?, ?)", clientes_data)
cursor.executemany("INSERT INTO faturas VALUES (?, ?, ?, ?, ?)", faturas_data)

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