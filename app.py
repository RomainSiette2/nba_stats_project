import streamlit as st
import pandas as pd 

st.title("🏀 Mon Dashboard NBA")

st.markdown("Bienvenue dans cette application interactive construite avec Streamlit !")

joueur_saisi = st.text_input("Entrez le nom d'un joueur actif :")

if joueur_saisi:
    st.write(f"✅ Vous avez sélectionné : **{joueur_saisi}**")


liste_joueurs = ["LeBron James", "Stephen Curry", "Kevin Durant"]
joueur_selectionne = st.selectbox("Ou choisissez un joueur dans la liste :", liste_joueurs)


st.write(f"👀 Joueur choisi dans le menu : **{joueur_selectionne}**")

df_demo = pd.DataFrame({
    "Match": ["Match 1", "Match 2", "Match 3"],
    "Points": [28, 35, 22],
    "Rebonds": [8, 5, 10],
    "Passes": [7, 9, 6]
})

st.subheader("📊 Stats fictives :")
st.dataframe(df_demo)


st.subheader("📈 Évolution des points :")
st.line_chart(df_demo["Points"])