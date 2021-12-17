
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs
import pages.support as sp



def app():

    portada = Image.open("images/Restaurant finder.jpg")
    st.image(portada, use_column_width=True)

    
    st.write("""
    #### "La Cucharona" consiste en un buscador de restaurantes para Madrid, en función de una ubicación dada y el tipo de restaurante elegido por el usuario.
    """)

    st.write("""
    ### TECNOLOGÍAS Y LIBRERIAS
    """)
    st.write("""
    #### 
    - Web scraping Selenium [tripadvisor](https://www.tripadvisor.es/)
    - Limpieza de datos
    - Llamadas a API (GeoPy)
    - Creación de base de datos en MongoDB Compass
    - Streamlit: Buscador de restaurantes 
    - Visualización: Folium y Kepler
    ### 
    """)


    
















