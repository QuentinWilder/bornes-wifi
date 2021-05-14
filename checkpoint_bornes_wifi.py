import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

st.title('Bornes Wifi à Toulouse')

path = '/home/atar/DataScience/WCS/checkpoint_2/bornes-wi-fi.csv'
df_bornes_wifi = pd.read_csv(path, sep=';')

df_bornes_wifi['geo_point'] = df_bornes_wifi['Geo Point'].apply(lambda x: [float(x.split(',')[0]), float(x.split(',')[1])])

coord_hotel_ville = [43.604704881866475, 1.4439313404444625]

map_bornes_wifi = folium.Map(location=coord_hotel_ville, zoom_start=13, tiles='CartoDB Positron')

for index, row in df_bornes_wifi.iterrows():
    if "intérieur" in row['zone_emission']:
        folium.Marker(location=row['geo_point'],
                      popup=row['site'],
                      icon=folium.Icon(color="green"),
                     ).add_to(map_bornes_wifi)
    else:
        folium.Marker(location=row['geo_point'],
                      popup=row['site'],
                      icon=folium.Icon(color="cadetblue"),
                     ).add_to(map_bornes_wifi)

folium_static(map_bornes_wifi)
