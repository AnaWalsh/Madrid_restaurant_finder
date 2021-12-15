import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs
import pages.support as sp

def app():
    #portada = Image.open("images/portada2.jpg")
    #st.image(portada, use_column_width=True)
    st.write("""
    # La Cucharona 🥄 
    ## 
    ...
    """)
    #f=codecs.open("data/pedrito.html", 'r')
    #pedro = f.read()

    #components.html(pedro,height=550,scrolling=True)

       
    #input de ubicacion del usuario
    location = st.text_input("¿Dónde estás?", "Paseo de la Chopera 14")
    #coordinate = mp.get_coordenadas(location)

    #input de distancia que quiere caminar
    distance = st.text_input("¿Cuántos metros quieres caminar?", "500")
    

    #input del tipo de comida
    df = sp.load_data()
    food_type = sp.get_uniques(df)


    food_type_ = st.selectbox("¿Qué tipo de restaurante te apetece?", ["Elige un tipo"] + food_type)

    coord = sp.get_coordenadas(location)

    df = sp.query(distance, coord, food_type_)
 


    if food_type_ == "Elige un tipo": 
        st.write("we need info")
    else:
        df_map= sp.query_for_map(distance, coord, food_type_)
        print(df_map.columns)
        st.dataframe(df)
        sp.map(df_map, coord)
