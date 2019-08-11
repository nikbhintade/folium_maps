# importing required modules
import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.csv")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data["ELEV"])


def color_producer(el):
    if el <= 2000:
        return "green"
    elif 2000 < el <= 3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[38, -100], zoom_start=6, tiles="Mapbox Bright ")

fg = folium.FeatureGroup(name="my Feature")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(
        location=[lt, ln], radius=6, popup=str(el) + " m", fill_color=color_producer(el), color='grey', fill_opacity=0.7))

fg.add_child(folium.GeoJson(
    data=(open('world.json', 'r', encoding='utf-8-sig').read()),
    style_function=lambda x: {
        'fillColor': 'yellow' if x['properties']['POP2005'] <= 10000000 else 'green'
        if 10000000 < x['properties']['POP2005'] <= 30000000 else 'red'
        if 30000000 < x['properties']['POP2005'] <= 50000000 else 'blue'}))


map.add_child(fg)
map.add_child(folium.LayerControl())

map.save("map_1.html")
