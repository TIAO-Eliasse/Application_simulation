import streamlit as st
st.write("###                                     Theme")
st.write("##### Mecanisme de transmissions des flucutuations des prix de pétroles dans l'économie de la Guinée Equatoriale")
st.image("OIP.jpg", caption="Guinée Equatoriale", use_column_width=True)
st.markdown("Cette application a été réalisé par:")

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
    st.switch_page("pages/1_AnalyseExploratoire.py")
