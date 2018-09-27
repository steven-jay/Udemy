import folium
import pandas as pd

def colorByElevation(elevation):
    if elevation > 3000:
        return '#F5634A'
    elif 1000 <= elevation < 3000:
        return '#FAD089'
    else:
        return '#3B8183'

data = pd.read_csv('./app2-web-map/Volcanoes_USA.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
name = list(data['NAME'])
elevation = list(data['ELEV'])

maps = folium.Map(location=[0,0], zoom_start = 3)

fgv = folium.FeatureGroup(name='Volcanoes')
fgp = folium.FeatureGroup(name='Population')

for lt, ln, nm, el in zip(lat, lon, name, elevation):
    # fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(nm, parse_html=True), icon=folium.Icon(color=colorByElevation(el))))
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 10,\
    popup=folium.Popup(nm, parse_html=True), \
    color=colorByElevation(el), fill=True, fill_opacity=0.7))

fgp.add_child(folium.GeoJson(data=open('./app2-web-map/world.json', 'r', \
encoding='utf-8-sig').read(), style_function=(lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 \
else 'orange' if 10000000 <= x['properties']['POP2005'] < 100000000 else 'red'})))

maps.add_child(fgv)
maps.add_child(fgp)
maps.add_child(folium.LayerControl()) # must be added after feature group so that layer control can refer to feature group

maps.save('Map.html')
