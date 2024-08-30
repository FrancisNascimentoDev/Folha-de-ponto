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
