import streamlit as st
import os
from PIL import Image
def data_dir(data_name):
    main=os.path.dirname(__file__)
    return os.path.join(main,data_name)
imag_path=data_dir("OIP.jpg")
st.write("###                                     Theme")
st.write("##### Mecanisme de transmissions des flucutuations des prix de pétroles dans l'économie de la Guinée Equatoriale")
#st.image(Image.open(imag_path), caption="Guinée Equatoriale", use_column_width=True)

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
