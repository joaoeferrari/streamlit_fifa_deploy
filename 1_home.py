import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime
import openia


if "data" not in st.session_state:
    df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year ] #clubes atuais - contrato valido com datas superiores a de hoje
    df_data = df_data[df_data["Value(£)"]>0] #pegar os melhores jogadores - excluindo jogadores sem valores registrados
    df_data = df_data.sort_values(by="Overall", ascending=False) #ordenar pelo overwall
    st.session_state["data"] = df_data


st.markdown('# FIFA23 OFFICIAL DATASET⚽')
# criando a sidebar - usando a "fonte" markdown - colocando o link dentro da sidebar
st.sidebar.markdown('Desenvolvido por [Asimov Academy](https://asimov.academy)')

btn = st.button('Acesse os dados no Kaggle')
if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/stefanoleone992/fifa-23-complete-player-dataset')

st.markdown(
    """
    O conjunto de dados de jogadores de futebol de 2017 a 2023 fornece informações abrangentes sobre jogadores de futebol profissionais. O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos do jogador, características físicas, estatísticas de jogo, detalhes do contrato e afiliações de clubes.body=
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para analistas de futebol, pesquisadores e entusiastas interessados em explorar vários aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e desenvolvimento do jogador ao longo do tempo.
    """  
)