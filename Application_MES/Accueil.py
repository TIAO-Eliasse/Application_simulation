import streamlit as st
st.title("Application Simulation ")
st.write("## Mecanisme de transmissions des flucutuations des prix de pétroles dans l'économie de la Guinée Equatoriale")

st.markdown("Cette application a été par:")

st.write(" TIAO Eliasse")
st.write("Amos Santiago")

st.markdown("""
    <style>
    .stButton button {background-color: green;
        color: white;
        padding-top: 20px;
        padding-bottom:40px;
    }
    </style>
    """, unsafe_allow_html=True)
if st.button("Continuez"):
    st.switch_page("Pages/1_AnalyseExploratoire.py")
