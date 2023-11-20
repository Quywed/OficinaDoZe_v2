import sqlite3

# CONEXAO
conn = sqlite3.connect('oficina.db')

# CURSOR PARA EXECUTAR QUERYS
cursor = conn.cursor()

#TABELA
cursor.execute('''
               
    
''')



#INSERTS
cursor.executemany("INSERT INTO **** (field1, field2) VALUES (?, ?)", users_data)

#LISTAR
cursor.execute("SELECT * FROM _nome_tabela;")
tables = cursor.fetchall()

print(type(tables))

for i in tables:
    print(f"Username: {i[0]}, Email: {i[1]}")

conn.commit() #COMITT
conn.close() #FECHAR A CONEXAO