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

# INSERTS
veiculos_data = []
clientes_data = []
empregados_data = []
faturas_data = []

for e in range(2):
    password_empregado = "password_empregado"  # Change this to your password logic
    password_hash_empregado = hashlib.sha256(password_empregado.encode()).hexdigest()
    empregados_data.append((e + 1, f'Empregado{e}', f'empregado{e}@email.com', password_hash_empregado))

cursor.executemany("INSERT INTO empregados VALUES (?, ?, ?, ?)", empregados_data)

for c in range(2):
    password_cliente = "password_cliente"  # Change this to your password logic
    password_hash_cliente = hashlib.sha256(password_cliente.encode()).hexdigest()
    cliente_random = random.randint(1000, 9999)
    clientes_data.append((cliente_random, f'Cliente{c}', f'cliente{c}@email.com', '123456789', password_hash_cliente))

for v in range(2):
    matricula_random = f"ABC{random.randint(100, 999)}"
    cliente_random = random.choice(clientes_data)[0]
    veiculos_data.append((matricula_random, 'Modelo', 'Marca1', 2020, 50000, 'Motor1', cliente_random))

for f in range(2):
    faturas_random = random.randint(1000, 9999)
    cliente_random = random.choice(clientes_data)[0]
    faturas_data.append((faturas_random, cliente_random, datetime.now(), 'Servico1', 100.00))

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