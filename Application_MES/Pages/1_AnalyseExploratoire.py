import streamlit as st
import pandas as pd

st.markdown("""
<style>
/* Ajuste la largeur totale du conteneur principal */
[data-testid="stAppViewContainer"] {
    max-width: 100%; /* Ajustez la largeur à 95% de l'écran */
    padding-left: 0rem; /* Supprime les marges latérales */
    padding-right: 0rem;
    margin-left: auto;
    margin-right: auto;
}

/* Réduit les marges des blocs pour un meilleur alignement */
[data-testid="block-container"] {
    padding: 1rem 0rem; /* Ajoute un espacement en haut et en bas uniquement */
}

/* Permet d'afficher plusieurs graphiques sur une même ligne */
[data-testid="stHorizontalBlock"] > div {
    flex: 1; /* Répartit l'espace horizontalement */
    margin-right: 1rem; /* Ajoute un espace entre les colonnes */
}

/* Améliore la gestion des composants interactifs */
[data-testid="stSidebar"] {
    padding-left: 0rem;
    padding-right: 0rem;
}
</style>
""", unsafe_allow_html=True)

st.write("Mecanisme de transmission des fluctuations des prix de pétrole dans l'économmie de la Guinée Equatoriale")



# CSS personnalisé pour l'arrière-plan
st.markdown("""
    <style>
    .stApp {
        background-color: #eaf6ff; /* Bleu clair inspiré de Stata */
    }
    .sidebar .sidebar-content {
        background-color: #d0e6f5; /* Bleu encore plus clair pour la barre latérale */
    }
    h1, h2, h3, h4, h5, h6 {
        color: #1f77b4; /* Bleu Stata pour les titres */
    }
    .stButton>button {
        background-color: #1f77b4; /* Boutons Stata */
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)






