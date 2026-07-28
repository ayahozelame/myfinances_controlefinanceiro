import mysql.connector #Importando a biblioteca para usar o MySQL

def conectar_banco():
   #Estabelecendo a conexão com o servidor MySQL e retornando o objeto de conexão.
    try:
        conexao = mysql.connector.connect(
            host="localhost",          
            user="root",        
            password="admin",      
            database="controle_financeiro"  
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    
#Criando a função de criar tabela quando não existir
def criar_tabela():
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        
        query = """
        CREATE TABLE IF NOT EXISTS transacoes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            descricao VARCHAR(50),
            valor DECIMAL(10,2),
            data DATE,
            categoria VARCHAR(20),
            tipo ENUM('Receita', 'Despesa')
        );
        """
        
        try:
            cursor.execute(query)
            conexao.commit() # Confirma as alterações no banco
            print("Tabela verificada/criada com sucesso!")
        except mysql.connector.Error as erro:
            print(f"Erro ao criar tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()

#Criando a função de inserir as transações
def inserir_transacoes(descricao, valor, data, categoria, tipo):
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()

        query = """
        INSERT INTO transacoes(
        descricao, valor, data, categoria, tipo)
        VALUES
        (%s, %s, %s, %s, %s)
"""
        try:
            cursor.execute(query, (descricao, valor, data, categoria, tipo))
            conexao.commit()
            print("Valores inseridos com sucesso!")
        except mysql.connector.Error as erro:
            print(f'Erro ao inserir dados na tabela:{erro}')
        finally:
            cursor.close()
            conexao.close()

#Criando a função de listar as transações
def listar_transacoes():
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()

        query = """
        SELECT * FROM transacoes;
"""

        try: 
            cursor.execute(query)
            dados = cursor.fetchall()
            print("Listagem completa com sucesso!")
            return dados
        except mysql.connector.Error as erro:
            print(f'Erro ao listar transações:{erro}')
        finally:
            cursor.close()
            conexao.close()
   

#Criando a função para limpar a tabela
def limpar_tabela():
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute("TRUNCATE TABLE transacoes;")
            conexao.commit()
            print("Tabela limpa com sucesso!")
        except mysql.connector.Error as erro:
            print(f"Erro ao limpar tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()

#Criando a função para deletar alguma transação através do ID.
def deletar_transacao(id):
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()

        query = """
        DELETE FROM transacoes 
        WHERE id = %s """

        try:
            cursor.execute(query, (id,))
            conexao.commit()
            print('Transação apagada com sucesso!')
        except mysql.connector.Error as erro:
            print(f'Erro ao apagar transação:{erro}')
        finally:
            cursor.close()
            conexao.close()








