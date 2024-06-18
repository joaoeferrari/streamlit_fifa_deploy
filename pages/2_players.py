import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃",
    layout="wide"
)


df_data = st.session_state['data']
# df_data

clubes  = df_data["Club"].value_counts().index  #filtrando a coluna "Clubes" do df acima - com "valores" únicos
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[(df_data["Club"] == club)]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)

player_stats = df_data[df_data["Name"] == player].iloc[0] #pegando a primeira aparição do jogador - caso ele apareça mais de uma vez no conjunto de dados

st.image(player_stats["Photo"])
st.title(player_stats["Name"])

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}") #formatando altura
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] *0.453:.2f}") #formatando peso 
st.divider() # equivale ao hr

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))

col5, col6, col7, col8 = st.columns(4)
col5.metric(f"Valor de mercado", value=f"£ {player_stats['Value(£)']}")
col6.metric(f"Remuneração semanal", value=f"£ {player_stats['Wage(£)']}")  
col7.metric(f"Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']}")