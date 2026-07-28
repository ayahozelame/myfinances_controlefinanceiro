#Importando as bibliotecas necessárias
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
#Importando as tabelas do banco de dados
from database.conexao import inserir_transacoes, listar_transacoes, deletar_transacao

st.set_page_config(page_title="MyFinances | Controle Financeiro", layout="wide") #Definindo o nome da página

st.title("💰 Meu Controle Financeiro") #Definindo o título da página
st.markdown("---") #Apenas para separar os itens

#Criando o Menu Lateral
st.sidebar.title("Navegação")
tela_selecionada = st.sidebar.radio(
    "Ir para:",
    ["📊 Dashboard", "➕ Nova Transação", "📋 Histórico"]
)

#Exibição das telas
if tela_selecionada == "📊 Dashboard":
    dados = listar_transacoes()
    
    if dados:
        df = pd.DataFrame(dados, columns=["ID", "Descrição", "Valor (R$)", "Data", "Categoria", "Tipo"])
        df["Valor (R$)"] = pd.to_numeric(df["Valor (R$)"])
        
        #Criando as 3 colunas principais lado a lado no topo
        col1, col2, col3 = st.columns(3)

        #Primeiro coluna com o valor das despesas, receitas e saldo final
        with col1:
            st.subheader("Painel Geral")
            total_receitas = df[df["Tipo"] == "Receita"]["Valor (R$)"].sum()
            total_despesas = df[df["Tipo"] == "Despesa"]["Valor (R$)"].sum()
            saldo = total_receitas - total_despesas

            st.metric(label="Total Receitas", value=f"R$ {total_receitas:.2f}")
            st.metric(label="Total Despesas", value=f"R$ {total_despesas:.2f}")
            st.metric(label="Saldo Final", value=f"R$ {saldo:.2f}")

        #Segunda coluna com a tabela das despesas por categoria
        with col2:
            st.subheader("Despesas por Categoria")
            df_despesas = df[df["Tipo"] == "Despesa"]
            df_categorias = df_despesas.groupby("Categoria")["Valor (R$)"].sum().reset_index()
            
            st.dataframe(df_categorias, use_container_width=True)

        #Terceira coluna com o gráfico
        with col3:
            st.subheader("Visualização Geral")
            if not df_categorias.empty and df_categorias["Valor (R$)"].sum() > 0:
                fig, ax = plt.subplots()
                fig.patch.set_alpha(0.0)
                ax.patch.set_alpha(0.0)

                ax.pie(
                    df_categorias["Valor (R$)"], 
                    labels=df_categorias["Categoria"], 
                    autopct='%1.1f%%',  
                    textprops={'color': 'white'}
                )
                st.pyplot(fig, transparent=True)
            else:
                st.info("Sem despesas cadastradas para exibir gráfico.")
    else:
        st.info("Nenhuma transação encontrada no banco de dados.")


elif tela_selecionada == "➕ Nova Transação":
    st.subheader("Cadastrar Transação")

    descricao = st.text_input("Descrição (Ex: Aluguel, Mercado):")
    valor = st.number_input("Valor (R$):", min_value=0.0, format="%.2f")
    data = st.date_input("Data do Lançamento:")
    categoria = st.selectbox("Categoria", ["Alimentação", "Moradia", "Lazer", "Trabalho", "Telefone/Internet", "Outros"])
    tipo = st.selectbox("Tipo de Transação:", ["Receita", "Despesa"])

    if st.button("Salvar Transação"):
        if descricao and valor > 0:
            inserir_transacoes(descricao, valor, str(data), categoria, tipo)
            st.success("Transação salva com sucesso! 🎉")
            st.rerun()
        else:
            st.warning("Preencha a descrição e um valor maior que zero!")


elif tela_selecionada == "📋 Histórico":
    st.subheader("Histórico de Lançamentos")
    
    dados = listar_transacoes()
    
    if dados:
        df = pd.DataFrame(dados, columns=["ID", "Descrição", "Valor (R$)", "Data", "Categoria", "Tipo"])
        df["Valor (R$)"] = pd.to_numeric(df["Valor (R$)"])
        
        #Cabeçalho da tabela no Histórico
        c_desc, c_val, c_data, c_cat, c_tipo, c_acao = st.columns([2.5, 1.5, 1.5, 1.5, 1.5, 0.8])
        c_desc.write("**Descrição**")
        c_val.write("**Valor**")
        c_data.write("**Data**")
        c_cat.write("**Categoria**")
        c_tipo.write("**Tipo**")
        c_acao.write("**Excluir**")
        st.markdown("---")
        
        #For para definir as linhas
        for index, linha in df.iterrows():
            col_desc, col_val, col_data, col_cat, col_tipo, col_acao = st.columns([2.5, 1.5, 1.5, 1.5, 1.5, 0.8])
            
            col_desc.write(linha["Descrição"])
            col_val.write(f"R$ {linha['Valor (R$)']:.2f}")
            col_data.write(str(linha["Data"]))
            col_cat.write(linha["Categoria"])
            col_tipo.write(linha["Tipo"])
            
            with col_acao:
                if st.button("🗑️", key=f"btn_del_{linha['ID']}"):
                    deletar_transacao(linha["ID"])
                    st.success("Excluído com sucesso!")
                    st.rerun()
    else:
        st.info("Nenhuma transação cadastrada no histórico.")


