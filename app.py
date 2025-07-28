import streamlit as st
import pandas as pd
from fonctions import get_data_frame, mean_win_loss, barplot_WL, find_all_players, player_avg_stats, get_player_id, get_player_season

st.set_page_config(layout="wide")

all_players = find_all_players()

default_player = "Victor Wembanyama"
index = all_players.index(default_player)


st.sidebar.title("Filtres")

player = st.sidebar.selectbox("Choisir un joueur:",all_players, index=index)
player_id = get_player_id(player)
season_list = get_player_season(player_id)
season = st.sidebar.selectbox("Choisir la saison :", season_list)



st.title("🏀 Mon Dashboard NBA")



tab1, tab2 = st.tabs(["Présentation","Saison"])


with tab1 :
    st.write("je suis le premier onglet ")


with tab2 :
    st.title(f"Statistiques de {player} lors de la saison {season}")
    with st.container():
        col1, col2, col3 = st.columns(3)
        avg_pts, avg_reb, avg_ast = player_avg_stats(player,season)
        col1.metric("🏀 Points", avg_pts)
        col2.metric("🛡️ Rebonds", avg_reb)
        col3.metric("🎯 Passes", avg_ast)

    col1 , col2 = st.columns(2)

    fig = barplot_WL(player, season)
    col1.pyplot(fig)

   




