#!pip install folium
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import folium
pd.set_option('display.max_columns', None)

#data import
flightdata1 = pd.read_excel('case3/30Flight 1.xlsx')
flightdata2 = pd.read_excel('case3/30Flight 2.xlsx')
flightdata3 = pd.read_excel('case3/30Flight 3.xlsx')
flightdata4 = pd.read_excel('case3/30Flight 4.xlsx')
flightdata5 = pd.read_excel('case3/30Flight 5.xlsx')
flightdata6 = pd.read_excel('case3/30Flight 6.xlsx')
flightdata7 = pd.read_excel('case3/30Flight 7.xlsx')

#kleur voor de hoogte
def flkleur(hoogte):
    if hoogte > 40000:
        return 'purple'
    elif hoogte > 30000:
        return 'blue'
    elif hoogte > 20000:
        return 'dodgerblue'
    elif hoogte > 10000:
        return 'lawngreen'
    elif hoogte > 8000:
        return 'greenyellow'
    elif hoogte > 4000:
        return 'yellow'
    elif hoogte > 2000:
        return 'gold'
    else:
        return 'red'

# Select flight data
flightdata_options = {
    'Flight 1': flightdata1,
    'Flight 2': flightdata2,
    'Flight 3': flightdata3,
    'Flight 4': flightdata4,
    'Flight 5': flightdata5,
    'Flight 6': flightdata6,
    'Flight 7': flightdata7
}

selected_flight = st.selectbox('Select Flight Data', list(flightdata_options.keys()))
flightdata = flightdata_options[selected_flight]

# Create map for selected flight
m = folium.Map(location=[52.303928, 4.765694], zoom_start=5)
folium.TileLayer(tiles="cartodbpositron", name="Grijze kaart").add_to(m)

for i in flightdata.index:
    folium.Circle(
        location=[flightdata.loc[i, "[3d Latitude]"], flightdata.loc[i, "[3d Longitude]"]],
        popup=f"Heading: {flightdata.loc[i, '[3d Heading]']}, Speed: {flightdata.loc[i, 'TRUE AIRSPEED (derived)']}, Hoogte: {flightdata.loc[i, '[3d Altitude Ft]']}",
        color=flkleur(flightdata.loc[i, "[3d Altitude Ft]"]),
        fill=True,
        fill_color=flkleur(flightdata.loc[i, "[3d Altitude Ft]"]),
        radius=500
    ).add_to(m)

m
