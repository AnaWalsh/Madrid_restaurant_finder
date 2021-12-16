import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs

from streamlit.type_util import data_frame_to_bytes
import pages.support as sp
import pandas as pd


def app():
    #portada = Image.open("images/portada2.jpg")
    #st.image(portada, use_column_width=True)
    st.write("""
    # Un resumen de lo que tenemos en madrid
    """)



#sp.graph_1(df)


