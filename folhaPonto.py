import sqlite3
from datetime import datetime

# Função para criar conexão com o banco de dados
def criar_conexao():
    return sqlite3.connect('folha_ponto.db')

# Função para criar as tabelas necessárias
def criar_tabelas():
    conn = criar_conexao()
    cursor = conn.cursor()
    
    # Criar tabela para os dados da empresa
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empresa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cnpj TEXT NOT NULL
        )
    ''')
    
    # Criar tabela para os dados dos funcionários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            matricula TEXT NOT NULL,
            empresa_id INTEGER,
            FOREIGN KEY (empresa_id) REFERENCES empresa (id)
        )
    ''')
    
    # Criar tabela para os registros de horários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ponto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            funcionario_id INTEGER,
            data TEXT,
            entrada TEXT,
            almoco_saida TEXT,
            almoco_retorno TEXT,
            saida TEXT,
            FOREIGN KEY (funcionario_id) REFERENCES funcionario (id)
        )
    ''')
    
    conn.commit()
    conn.close()

# Função para cadastrar uma empresa
def cadastrar_empresa():
    nome = input("Digite o nome da empresa: ")
    cnpj = input("Digite o CNPJ da empresa: ")
    
    conn = criar_conexao()
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO empresa (nome, cnpj) VALUES (?, ?)', (nome, cnpj))
    
    conn.commit()
    conn.close()
    print(f"Empresa '{nome}' cadastrada com sucesso!")

# Função para cadastrar um funcionário
def cadastrar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    matricula = input("Digite a matrícula do funcionário: ")
    empresa_id = input("Digite o ID da empresa: ")
    
    conn = criar_conexao()
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO funcionario (nome, matricula, empresa_id) VALUES (?, ?, ?)', (nome, matricula, empresa_id))
    
    conn.commit()
    conn.close()
    print(f"Funcionário '{nome}' cadastrado com sucesso!")

# Função para registrar ponto do funcionário
def registrar_ponto():
    funcionario_id = input("Digite o ID do funcionário: ")
    entrada = input("Digite o horário de entrada (HH:MM): ")
    almoco_saida = input("Digite o horário de saída para almoço (HH:MM): ")
    almoco_retorno = input("Digite o horário de retorno do almoço (HH:MM): ")
    saida = input("Digite o horário de saída (HH:MM): ")
    
    conn = criar_conexao()
    cursor = conn.cursor()
    
    data_atual = datetime.now().strftime('%Y-%m-%d')
    
    cursor.execute('''
        INSERT INTO ponto (funcionario_id, data, entrada, almoco_saida, almoco_retorno, saida)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (funcionario_id, data_atual, entrada, almoco_saida, almoco_retorno, saida))
    
    conn.commit()
    conn.close()
    print(f"Ponto registrado para o funcionário ID {funcionario_id} na data {data_atual}.")

# Função para exibir todos os pontos registrados
def exibir_pontos():
    conn = criar_conexao()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT f.nome, p.data, p.entrada, p.almoco_saida, p.almoco_retorno, p.saida
        FROM ponto p
        JOIN funcionario f ON p.funcionario_id = f.id
    ''')
    
    pontos = cursor.fetchall()
    
    for ponto in pontos:
        print(f'Funcionário: {ponto[0]}, Data: {ponto[1]}, Entrada: {ponto[2]}, Saída Almoço: {ponto[3]}, Retorno Almoço: {ponto[4]}, Saída: {ponto[5]}')
    
    conn.close()

# Menu para interação com o usuário
def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar Empresa")
        print("2. Cadastrar Funcionário")
        print("3. Registrar Ponto")
        print("4. Exibir Pontos Registrados")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_empresa()
        elif opcao == '2':
            cadastrar_funcionario()
        elif opcao == '3':
            registrar_ponto()
        elif opcao == '4':
            exibir_pontos()
        elif opcao == '5':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Criar tabelas ao iniciar o script
criar_tabelas()

# Iniciar o menu
menu()
