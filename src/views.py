from clientes import *
from faturas import *
from veiculos import *



conn = sqlite3.connect('src/oficina.db')

    # CURSOR PARA EXECUTAR QUERYS
cursor = conn.cursor()

imprime_lista_de_clientes(conn)