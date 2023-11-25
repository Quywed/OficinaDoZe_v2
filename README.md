# Oficina do Zé - Sistema de Gestão para Oficina de Automóveis.

Bem-vindo ao projeto Oficina do Zé! Este sistema foi projetado para gerir clientes, veículos e faturas numa oficina.

## Introdução

Este projeto pretende fornecer uma interface simples de linha de comando para gerir uma oficina. Utiliza o SQLite para armazenamento da base de dados e inclui funcionalidades para clientes, veículos e faturas.

## Recursos

- **Gestão de Clientes (clientes.py) :** Funções para gestão de clientes.
- **Gestão de Veículos (veiculos.py) :** Funções para gestão de veículos de clientes.
- **Gestão de Faturas (faturas.py) :** Funções para gestão de faturas dos serviço.
- **Gestão de Empregados (empregado.py )** Funções para gestão de empregados.

## Step-by-step como iniciar o programa

Para executar o programa, tem de garantir que a base de dados da oficina esteja criada, e com ao menos alguns inserts de registos nas tabelas. Para mais informações, aceda à página de informação sobre o [ficheiro da base de dados](https://github.com/Quywed/OficinaDoZe_v2/wiki/Base-de-Dados).

### Linguagens e Bibliotecas usadas

- Python  | linguagem dos scripts criados
- SQLite  | biblioteca em linguagem C que implementa uma base de dados SQL embutida
- Hashlib | bilbioteca que implementa uma interface comum para muitos algoritmos criptográficos seguros de hash e de digestão de mensagens
- Getpass | biblioteca que contém uma função que permite esconder a password

### Instalação

Para conseguir executar os ficheiros, é necessário ter um IDE instalado com algum tipo de intrepretador de python instalado no mesmo. Recomendamos o **Visual Studio Code** com o Interpretador de Python **Anaconda**.

Após ter realizado os passos anteriores, é necessário ter o módulo de **SQLITE3** instalado. Por defeito deve vir instalado com o Python, mas caso a versão seja anterior à Python 3.0, na linha de comandos, execute o seguinte comando:

```
pip install pysqlite3
```

Quando estiver no VSCODE, para clonar o repositório, siga os seguintes passos:

1. Abrir a palette de comandos com a combinação de teclas **Ctrl + Shift + P**.

2. Selecionar a opção **Git Clone**

3. Inserir o URL do repositório:

```
   git clone [https://github.com/seu-nome-de-usuário/oficina-do-ze.git](https://github.com/Quywed/OficinaDoZe_v2.git)
```

4. Selecionar a pasta/diretoria no seu computador para onde os ficheiros irão ser clonados

Se tiver realizado estes passos, os ficheiros devem ter sido clonados com sucesso para a pasta que selecionou no último passo

