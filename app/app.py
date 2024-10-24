import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# def exibir_tabela_dados(data):
#     """
#         Exibe a table CSV carregada

#         Parâmetros:
#             data: DataFrame referente ao CSV carregado

#     """

#     st.subheader("Dados de origem")
#     st.dataframe(data)

def exibir_grafico_pessoas_genero(data):
    """
        Exibe o gráfico de pessoas por gênero

        Parâmetros:
            data: DataFrame referente ao CSV carregado

    """

    #gerando dataset de agrupamento de genero
    gender_counts = data['gender'].value_counts().rename_axis('gender').reset_index(name='counts')
    gender_counts.set_index('gender', inplace=True)

    #Gráfico do número de pessoas por gênero
    st.divider()
    st.subheader("Número de pessoas por gênero")
    st.bar_chart(gender_counts['counts'], x_label="Gêneros",y_label="Quantidade")

def exibir_agrupamento_geracao(data):

    """
        Exibe o gráfico de agrupamento por geração

        Parâmetros:
            data: DataFrame referente ao CSV carregado

    """

    #gerando dataset de agrupamento de geração
    generation_counts = data['generation'].value_counts().rename_axis('generation').reset_index(name='counts')
    generation_counts.set_index('generation', inplace=True)

    #Gráfico do número de pessoas por geração (horizontal)
    st.divider()
    st.subheader("Número de pessoas por geração")
    st.bar_chart(generation_counts['counts'], color= "#ffaa00",x_label="Geração",y_label="Quantidade", horizontal=True)

def exibir_media_educacao_genero(data):
    
    """
        Exibe o gráfico de média de educação por gênero

        Parâmetros:
            data: DataFrame referente ao CSV carregado

    """
    

    #gerando dataset de agrupamento de média de anos de educação por gênero
    gender_education_mean = data.groupby('gender')['years_of_education'].mean().reset_index(name='means')
    gender_education_mean.set_index('gender', inplace=True)

    #Gráfico da média de anos trabalhados
    st.divider()
    st.subheader("Média de anos trabalhados")
    st.bar_chart(gender_education_mean['means'], color= "#00aa00",x_label="Geração",y_label="Média de anos trabalhados")

def exibir_distribuicao_status_emprego(data):

    """
        Exibe a distribuição de status de emprego

        Parâmetros:
            data: DataFrame referente ao CSV carregado

    """

    #gerando dataset de estado atual de emprego
    job_counts = data['employment_status'].value_counts().rename_axis('employment_status').reset_index(name='counts')
    job_counts.set_index('employment_status', inplace=True)

    #Gráfico de pizza do Status de Emprego no Streamlit com o Plotly
    st.divider()
    st.subheader("Distribuição do Status de Emprego")

    fig = px.pie(job_counts, values='counts', names=job_counts.index)
    st.plotly_chart(fig)

def histograma_geral_idades(data):
    
    """
        Exibe o histograma geral de idades

        Parâmetros:
            data: DataFrame referente ao CSV carregado

    """

    # Criar faixas etárias
    data['age_group'] = pd.cut(data['age'], bins=[0, 18, 30, 45, 60, 100], labels=['0-18', '19-30', '31-45', '46-60', '61+'])

    #distribuição geral por idade
    age_group_counts = data['age_group'].value_counts().sort_index()

    #Mostra o histograma geral de idades
    st.divider()
    st.subheader("Distribuição por Idade")
    # Criando o gráfico de barras agrupadas
    fig_grouped_age = px.bar(age_group_counts,
                        labels={"value": "Número de Pessoas", "variable": "Idade"}, 
                        barmode='stack')

    fig_grouped_age.update_layout(
        xaxis_title="Idades"
    )

    st.plotly_chart(fig_grouped_age)

def histograma_geral_generos(data):

    """
        Exibe o histograma geral de gêneros

        Parâmetros:
            data: DataFrame referente ao CSV carregado

    """

    #distribuição por gênero e por idade
    age_gender_distribution = data.groupby(['age_group', 'gender'], observed=True).size().unstack(fill_value=0)

    #Mostra o histograma geral de idades agrupado por gênero
    st.divider()
    st.subheader("Distribuição por Idade e Gênero")
    # Criando o gráfico de barras agrupadas
    fig_grouped_gen = px.bar(age_gender_distribution,
                        labels={"value": "Número de Pessoas", "variable": "Idade"}, 
                        barmode='group')

    fig_grouped_gen.update_layout(
        xaxis_title="Idades"
    )

    st.plotly_chart(fig_grouped_gen)



#configurando o titulo da janela
st.set_page_config(page_title="Indicadores referente ao arquivo CSV", page_icon="👁")


#abre o arquivo manualmente


#exceção tratada para quando não tem carga de arquivo CSV  (para não dar erro no pdoc)
try:
    file = 'persons.csv'
    data = pd.read_csv(file)
    st.session_state["dataset"] = data

except FileNotFoundError:
    st.info("Por favor, faça o upload de um arquivo CSV para visualizar o mapa.")

st.title("Indicadores referente ao arquivo CSV")


#exibir_tabela_dados(data)


#exceção tratada para quando não tem carga de arquivo CSV  (para não dar erro no pdoc)
if "dataset" in st.session_state:

    exibir_grafico_pessoas_genero(st.session_state["dataset"])

    exibir_agrupamento_geracao(st.session_state["dataset"])

    exibir_distribuicao_status_emprego(st.session_state["dataset"])

    histograma_geral_idades(st.session_state["dataset"])

    histograma_geral_generos(st.session_state["dataset"])