import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs

from streamlit.type_util import data_frame_to_bytes
import pages.support as sp
import pandas as pd

from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster

from streamlit_folium import folium_static


def app():
    #portada = Image.open("images/portada2.jpg")
    #st.image(portada, use_column_width=True)
    st.write("""
    # ¿Cómo es la oferta de restaurantes en Madrid?
    """)
    portada = Image.open("file-20180918-158240-1jd9gm6.jpeg")
    st.image(portada, use_column_width=True)
    

    df_visual = sp.load_data2() #dataset groupby
    df_visual2 = sp.load_data() #dataset general
    st.write("mapa")

    
    sp.map_per_price(df_visual2)
    #folium_static(sp.map_per_price(df_visual2))



    st.write(""" ## Restaurantes clasificados por tipo """)
    st.plotly_chart(sp.graph_1(df_visual2))

    st.write(""" ## Restaurantes: tipo y precio """)
    st.plotly_chart(sp.graph_2(df_visual))


   



