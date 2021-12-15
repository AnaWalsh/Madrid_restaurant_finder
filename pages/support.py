import streamlit as st
from streamlit_folium import folium_static
import streamlit.components.v1 as components
import codecs
import folium
import requests
import pandas as pd
#import plotly_express as px
import folium
from folium import Choropleth, Circle, Marker, Icon, map
from streamlit_folium import folium_static


from pymongo import MongoClient
import requests
from dotenv import load_dotenv
import os
import pandas as pd
import geopandas as gpd
from cartoframes.viz import Map, Layer, popup_element
from functools import reduce
import operator
import json
import re
from geopy.geocoders import Nominatim


def load_data():
    return pd.read_csv('data/tripadvisor_latlon.csv')

def get_uniques(df):
    return list(df.type.unique())

def get_coordenadas(address):
    """
    Esta función saca las coordenadas de la ciudad que le pases.
    Args: una ciudad (string).
    Return: Las coordeandas de la ciudad que le paso como argumento (latitud y longitud).
    """
    geolocator = Nominatim(user_agent="Ana")
    location = geolocator.geocode(query=address, exactly_one=True)
    localizacion = location[1]
    return [localizacion[1], localizacion[0]]


def query(distance, coordinate, food_type):

    client = MongoClient("localhost:27017")
    db = client.get_database("PROJECT")
    collection = db["Restaurants"]
    collection.create_index([("type_point_", "2dsphere")])
    
    restaurants = db.get_collection("Restaurants")

    default_value_1 = "Paseo de la chopera 14, Madrid"
    default_value_2 = 100
 

    response = {"coordinates_v2": {"$near": {"$geometry":{'type': 'Point', 'coordinates':coordinate},
                                                  "$maxDistance": (int(distance))}},'type': food_type}

    df = pd.DataFrame(list(restaurants.find(response)))

    return df



'''

def map(df):

    map_1 = folium.Map(location=[inicial_lat,inicial_long], zoom_start=15)

    inicial_lat = coordinate[1]
    inicial_long = coordinate[0]

    dic = {"location": [inicial_lat, inicial_long], "tooltip": "ubicacion"}

    icono = Icon(color = "red",
                     prefix="fa",
                     icon="map-marker",
                     icon_color="black")


    for i,row in df.iterrows():

    #dic = {"location": [row["latitud"], row["longitud"]], "tooltip": row["nombre"]}
    dic = {"location": [row["latitud"], row["longitude"]], "tooltip": row["name"]}

    if row["type"] == "Mediterránea":
        icono = Icon(color = "green",
                     prefix="fa",
                     icon="circle",
                     icon_color="black")

    elif row["type"] == 'Italiana':
        icono = Icon(color = "lightblue",
                     prefix="fa",
                     icon="circle",
                     icon_color="black")

        
    elif row["type"] == "Internacional":        
        icono = Icon(color = "orange",
                     prefix="fa",
                     icon="circle",
                     icon_color="black")
           
    elif row["type"] == "Confiterías/panaderías":        
        icono = Icon(color = "gray",
                     prefix="fa",
                     icon="circle",
                     icon_color="black")
           
    elif row["type"] == "Japonesa":        
        icono = Icon(color = "cadetblue",
                     prefix="fa",
                     icon="circle",
                     icon_color="black")
           
           
    elif row["type"] == "Bar":        
        icono = Icon(color = "lightgreen",
                     prefix="fa",
                     icon="circle",
                     icon_color="black")
           
           
    elif row["type"] == "India":        
        icono = Icon(color = "lightblue",
                     prefix="fa",
                     icon="circle",
                     icon_color="black")           
           
    elif row["type"] == "Mexicana":        
        icono = Icon(color = "pink",
                     prefix="fa",
                     icon="circle",
                     icon_color="black")
           
           
    elif row["type"] == "Pub con cerveza artesanal":        
        icono = Icon(color = "purple",
                     prefix="fa",
                     icon="circle",
                     icon_color="black")
           
    
    mark = Marker(**dic, icon=icono)
    mark.add_to(map_1)

    folium_static(map_1)


    st.write("""
    ### Mapita insertado con HTML
    """)

    f=codecs.open("data/mapa.html", 'r')
    mapa = f.read()

    components.html(mapa,height=550,scrolling=True)   












def app():
    st.write("""
    ### Mapita de Folium
    """)
    default_value_goes_here = "Paseo de la chopera 14, Madrid"
    user_input = st.text_input("Introduce dirección", default_value_goes_here)

    data = requests.get(f"https://geocode.xyz/{user_input}?json=1").json()
    latlon = [data["latt"],data["longt"]]
    

    icono = folium.Icon(color="blue",
             prefix = "fa",
             icon="rocket",
             icon_color="black")


    datos = {"location": latlon, "tooltip": "Lo que buscas", "icon":icono}
    mark = folium.Marker(**datos)

    map_1 = folium.Map(location = latlon, zoom_start=15)
    mark.add_to(map_1)

    folium_static(map_1)


    st.write("""
    ### Mapita insertado con HTML
    """)

    f=codecs.open("data/mapa.html", 'r')
    mapa = f.read()

    components.html(mapa,height=550,scrolling=True)


'''
    