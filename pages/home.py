import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs
import pages.support as sp

def app():
    portada = Image.open("madrid-city-view.jpeg")
    st.image(portada, use_column_width=True)
    st.write("""
    # 
    ## 
    ...
    """)
    #f=codecs.open("data/pedrito.html", 'r')
    #pedro = f.read()

    #components.html(pedro,height=550,scrolling=True)

       
    #input de ubicacion del usuario
    location = st.text_input("", "Paseo de la Chopera 14 ") 
    #coordinate = mp.get_coordenadas(location)

    #input de distancia que quiere caminar
    distance = st.text_input("¿Cuántos metros quieres caminar?", "500")
    

    #input del tipo de comida
    df = sp.load_data()
    food_type = sp.get_uniques(df)


    food_type_ = st.selectbox("¿Qué tipo de restaurante te apetece?", ["Elige un tipo"] + food_type)

    coord = sp.get_coordenadas(location)

   


    if food_type_ == "Elige un tipo": 
        st.write("we need info")
        st.stop()
    elif food_type_ == "Todos los restaurantes": # condicion cuando queremos todos los restaurantes
        df_map_1 = sp.query_for_map2(distance, coord)
        if df_map_1.shape[0] == 0:
            st.write("oh oh...")
        else:
            df_mostrar = df_map_1.drop(["latitude", 'longitude'], axis = 1)
            st.dataframe(df_mostrar)
            st.write("tenemos" , df_mostrar.shape[0], "restaurantes")
            sp.map(df_map_1, coord)

    else: # condición cuando pasamos un filtro de comida
        df_map= sp.query_for_map(distance, coord, food_type_)
        if df_map.shape[0] == 0:
            st.write("oh oh...")
        else:
            df_mostrar = df_map.drop(["latitude", 'longitude'], axis = 1)
            st.dataframe(df_mostrar)
            st.write("tenemos" , df_mostrar.shape[0], "restaurantes")
            sp.map(df_map, coord)
