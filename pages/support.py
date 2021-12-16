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


import plotly.express as px
import seaborn as sns
import pandas as pd
import plotly.graph_objects as go


def load_data():
    return pd.read_csv('data/tripadvisor_latlon_v2.csv')

def load_data2():
    return pd.read_csv('data/plot1.csv')


def get_uniques(df):
    return ['Mediterránea', 'Bar', 'Asador', 'Café y postres', 'Europea',
       'Latina', 'Internacional', 'Italiana', 'Asiática', 'Marisco',
       'Americana', 'India', 'Otros', 'Mexicana', 'Filipina', 'Marroquí',
       'Fusión', 'Todos los restaurantes']

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
 
    print(distance)
    proyec = {"name": 1, "ranking":1, "price": 1,  "_id":0}
    response = {"coordinates_v2": {"$near": {"$geometry":{'type': 'Point', 'coordinates':coordinate},
                                                  "$maxDistance": (int(distance))}},'type': food_type}
    x = list(restaurants.find(response, proyec))
    return pd.DataFrame(x)


def query_for_map(distance, coordinate, food_type):

    client = MongoClient("localhost:27017")
    db = client.get_database("PROJECT")
    collection = db["Restaurants"]
    collection.create_index([("type_point_", "2dsphere")])
    
    restaurants = db.get_collection("Restaurants")

    default_value_1 = "Paseo de la chopera 14, Madrid"
    default_value_2 = 100
 
    proyec = { "_id":0, "name": 1, "ranking":1, "price_2": 1, "latitude":1, "longitude": 1, 'type': 1}
    response = {"coordinates_v2": {"$near": {"$geometry":{'type': 'Point', 'coordinates':coordinate},
                                                  "$maxDistance": (int(distance))}},'type': food_type}
    x2 = list(restaurants.find(response, proyec))
  
    return pd.DataFrame(x2)
    




def query_for_map2(distance, coordinate):

    client = MongoClient("localhost:27017")
    db = client.get_database("PROJECT")
    collection = db["Restaurants"]
    collection.create_index([("type_point_", "2dsphere")])
    
    restaurants = db.get_collection("Restaurants")

    default_value_1 = "Paseo de la chopera 14, Madrid"
    default_value_2 = 100
 
    proyec2 = { "_id":0, "name": 1, "ranking":1, "price_2": 1, "latitude":1, "longitude": 1, 'type': 1}
    response = {"coordinates_v2": {"$near": {"$geometry":{'type': 'Point', 'coordinates':coordinate},
                                                  "$maxDistance": (int(distance))}}}
    x2 = list(restaurants.find(response, proyec2))

    return pd.DataFrame(x2)
    


def map(df, coord):

    inicial_lat = coord[1]
    inicial_long =  coord[0]

    map = folium.Map(location=[inicial_lat,inicial_long], zoom_start=15)

    for i,row in df.iterrows():
    
        dic = {"location": [row["latitude"], row["longitude"]], "tooltip": row["name"]}

        if row["type"] == "Mediterránea":
            icono = Icon(color = "green",
                        prefix="fa",
                        icon="circle",
                        icon_color="black")

        elif row["type"] == "Bar":
            icono = Icon(color = "lightblue",
                        prefix="fa",
                        icon="circle",
                        icon_color="black")

            
        elif row["type"] == "Asador":        
            icono = Icon(color = "orange",
                        prefix="fa",
                        icon="circle",
                        icon_color="black")
            
        elif row["type"] == "Café y postres":        
            icono = Icon(color = "gray",
                        prefix="fa",
                        icon="circle",
                        icon_color="black")
            
        elif row["type"] == "Europea":        
            icono = Icon(color = "cadetblue",
                        prefix="fa",
                        icon="circle",
                        icon_color="black")
            
            
        elif row["type"] == "Latina":        
            icono = Icon(color = "lightgreen",
                        prefix="fa",
                        icon="circle",
                        icon_color="black")
            
            
        elif row["type"] == "Internacional":        
            icono = Icon(color = "lightblue",
                        prefix="fa",
                        icon="circle",
                        icon_color="black")           
            
        elif row["type"] == "Italiana":        
            icono = Icon(color = "pink",
                        prefix="fa",
                        icon="circle",
                        icon_color="black")
            
            
        elif row["type"] == "Asiática":        
            icono = Icon(color = "purple",
                        prefix="fa",
                        icon="circle",
                        icon_color="black")

        elif row["type"] == "Marisco":        
            icono = Icon(color = "purple",
                        prefix="fa",
                        icon="circle",
                        icon_color="black")

        elif row["type"] == "Americana":        
            icono = Icon(color = "purple",
                        prefix="fa",
                        icon="circle",
                        icon_color="black")

        elif row["type"] == "India":        
            icono = Icon(color = "purple",
                        prefix="fa",
                        icon="circle",
                        icon_color="black")

        elif row["type"] == "Mexicana":        
            icono = Icon(color = "purple",
                        prefix="fa",
                        icon="circle",
                        icon_color="black")


        elif row["type"] == "Filipina":        
            icono = Icon(color = "purple",
                        prefix="fa",
                        icon="circle",
                        icon_color="black")

        elif row["type"] == "Marroquí":       
            icono = Icon(color = "purple",
                        prefix="fa",
                        icon="circle",
                        icon_color="black")

        elif row["type"] == "Fusión":        
             icono = Icon(color = "purple",
                        prefix="fa",
                        icon="circle",
                        icon_color="black")

                    
        mark = Marker(**dic, icon=icono)
        mark.add_to(map)

    return folium_static(map)



def graph_1 (df):

    fig = px.bar(df, x=df.type.value_counts().index, y=df.type.value_counts().values)

    return fig


def graph_2 (df):

    fig = px.bar(df, x="type", y="price", color='price_2')
    return fig


def map_per_price2(df):

    inicial_lat = 40.4167047
    inicial_long =  -3.7035825

    map = folium.Map(location=[inicial_lat,inicial_long], zoom_start=15)

    for i,row in df.iterrows():
    
        dic = {"location": [row["latitude"], row["longitude"]], "tooltip": row["name"]}

        if row["price_2"] == "Medio":
            icono = Icon(color = "green",
                        prefix="fa",
                        icon="circle",
                        icon_color="black")

        elif row["price_2"] == "Barato":
            icono = Icon(color = "lightblue",
                        prefix="fa",
                        icon="circle",
                        icon_color="black")

            
        elif row["price_2"] == "Caro":        
            icono = Icon(color = "orange",
                        prefix="fa",
                        icon="circle",
                        icon_color="black")
            
        
            
        mark = Marker(**dic, icon=icono)
        mark.add_to(map)
    
    #return map
    return folium_static(map)
    