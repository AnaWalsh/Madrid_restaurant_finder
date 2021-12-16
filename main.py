from re import T
import streamlit as st
from PIL import Image
from multipage import MultiPage
from pages import home, user, presentation
#from pages import datos
#from pages import graficos
#from pages import mapas

app = MultiPage()

app.add_page("Search", home.app)
app.add_page("Data",user.app)
app.add_page("Presentacion", presentation.app)


app.run()