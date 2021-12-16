import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs
import pages.support as sp


def app():
    portada = Image.open("images/Restaurant finder.jpg")
    st.image(portada, use_column_width=True)
    st.write("""
    # 
    ## Encuentra el restaurante que quieras allá donde estés!! ⚡️
    """)
    #f=codecs.open("data/pedrito.html", 'r')
    #pedro = f.read()

    #components.html(pedro,height=550,scrolling=True)

    st.write("""
    ### Dónde estás? 📍
    """) 
    #input de ubicacion del usuario
    location = st.text_input("", "Paseo de la Chopera 14 ") 
    #coordinate = mp.get_coordenadas(location)



    st.write("""
    ### Cuánto estás dispuesto a andar?
    """) 
    #input de distancia que quiere caminar
    distance = st.text_input(" ", "500")
    

    #input del tipo de comida
    df = sp.load_data()
    food_type = sp.get_uniques(df)

    st.write("""
    ### Qué tipo de comida te apetece? 🍕🌮🍰🍤
    """) 
    food_type_ = st.selectbox(" ", ["Elige un tipo"] + food_type)

    coord = sp.get_coordenadas(location)

   


    if food_type_ == "Elige un tipo": 
        st.stop()
    elif food_type_ == "Todos los restaurantes": # condicion cuando queremos todos los restaurantes
        df_map_1 = sp.query_for_map2(distance, coord)
        if df_map_1.shape[0] == 0:
            st.write("Lo siento... no hemos encontrado ningún restaurante😢")
            st.write("Prueba haciendo una nueva búsqueda ⚡️")
        else:
            df_mostrar = df_map_1.drop(["latitude", 'longitude'], axis = 1)
            st.dataframe(df_mostrar)
            st.write("Hemos encontrado" , df_mostrar.shape[0], "restaurantes")
            sp.map(df_map_1, coord)
           
        
    

    else: # condición cuando pasamos un filtro de comida
        df_map= sp.query_for_map(distance, coord, food_type_)
        if df_map.shape[0] == 0:
            st.write("Lo siento... no hemos encontrado ningún restaurante 😢")
            st.write("Prueba haciendo una nueva búsqueda ⚡️")
        else:
            df_mostrar = df_map.drop(["latitude", 'longitude'], axis = 1)
            st.dataframe(df_mostrar)
            st.write("Hemos encontrado" , df_mostrar.shape[0], "restaurantes")
            sp.map(df_map, coord)
