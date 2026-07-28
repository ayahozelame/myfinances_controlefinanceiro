#💰MyFinances — Controle Financeiro

O MyFinances é uma aplicação web interativa para controle e análise de finanças pessoais. O sistema permite cadastrar receitas e despesas, acompanhar métricas de saldo em tempo real, analisar a distribuição de gastos por categoria através de gráficos e gerenciar o histórico completo de transações integrado a um banco de dados relacional MySQL.


#🎯Objetivo do Projeto

Este projeto foi desenvolvido com o propósito de aplicar conceitos práticos de Análise de Dados, Engenharia de Software e Visualização de Dados, construindo uma solução end-to-end (do banco de dados MySQL à interface gráfica com Streamlit) para resolução de um problema real do dia a dia.


🛠️Tecnologias Utilizadas

Linguagem: Python
Interface Gráfica: [Streamlit](https://streamlit.io/)
Manipulação de Dados: [Pandas](https://pandas.pydata.org/)
Visualização de Dados: [Matplotlib](https://matplotlib.org/)
Banco de Dados: MySQL (`mysql-connector-python`)


#🚀Funcionalidades

-📊Dashboard Interativo:
  - KPIs em Tempo Real: Visualização imediata de Total Receitas, Total Despesas e Saldo Final.
  - Tabela Agrupada: Sumarização e agrupamento de despesas por categoria.
  - Gráfico Dinâmico: Gráfico de pizza demonstrando a distribuição percentual dos gastos.

-➕Cadastro de Transações:
  - Formulário para inclusão de lançamentos (Descrição, Valor, Data, Categoria e Tipo).
  - Validação de entradas e persistência imediata no banco de dados.

-📋Histórico de Lançamentos (CRUD):
  - Listagem completa de todas as transações.
  - Exclusão unitária de registros com atualização dinâmica da interface (`st.rerun()`).


#🏗️Estrutura de Arquivos

```text
meu-controle-financeiro/
│── database/
│   ├── conexao.py         #Conexão MySQL e funções CRUD (INSERT, SELECT, DELETE)
│   └── schema.sql         #Script para criação do banco de dados e tabelas
│── app.py                 #Aplicação principal em Streamlit
│── requirements.txt       #Lista de dependências do Python
│── .gitignore             #Arquivos ignorados pelo Git
└── README.md              #Documentação do projeto
