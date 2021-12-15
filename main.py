from re import T
import streamlit as st
from PIL import Image
from multipage import MultiPage
from pages import home, user
#from pages import datos
#from pages import graficos
#from pages import mapas

app = MultiPage()

app.add_page("Que buscas", home.app)
app.add_page("Resumen datos",user.app)


app.run()