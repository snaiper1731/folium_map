import os
import datetime
import webbrowser
import folium
import pandas as pd
from tkinter import *
from tkinter.filedialog import askopenfilenames

file_names = askopenfilenames()

m = folium.Map(location=[51.673869103198385, 39.16847661268806], zoom_start=10)


for file_name in file_names:

    data_df = pd.read_excel(file_name)

    data_values = data_df["DATE"].unique()

    for data_value in data_values:
        #Приводим дату и время к читабельному виду
        convert_date = pd.to_datetime(str(data_value))
        formatted_date = convert_date.strftime('%Y-%m-%d')

        formatted_filename = os.path.basename(file_name)
        filename_without_extension = os.path.splitext(formatted_filename)[0]

        marker_layer =folium.FeatureGroup(f'{formatted_date}_{filename_without_extension}')

        unique_data_df = data_df[data_df["DATE"] == data_value]

        for index, row in unique_data_df.iterrows():
            name = row["NAME"]
            lat = row["LATITUDE"]
            lon = row["LONGITUDE"]
            desc = row["DESCRIPTION"]

            marker = folium.Marker(location=[lat, lon], popup=folium.Popup(desc, max_width=500), tooltip=name)
            marker.add_to(marker_layer)

        marker_layer.add_to(m)

folium.LayerControl().add_to(m)

m.save('map.html')
webbrowser.open('map.html')


