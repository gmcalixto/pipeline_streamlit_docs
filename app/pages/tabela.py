import streamlit as st


def exibir_tabela_dados(data):
    """
        Exibe a table CSV carregada

        Parâmetros:
            data: DataFrame referente ao CSV carregado

    """

    st.subheader("Dados de origem")
    st.dataframe(data)

st.title("Tabela CSV carregada")


#exceção tratada para quando não tem carga de arquivo CSV  (para não dar erro no pdoc)
if "dataset" in st.session_state:
    exibir_tabela_dados(st.session_state["dataset"])

else:
    st.info("Por favor, faça o upload de um arquivo CSV para visualizar o mapa.")