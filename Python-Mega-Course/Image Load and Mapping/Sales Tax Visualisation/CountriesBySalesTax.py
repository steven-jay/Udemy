import folium
import json
import pandas as pd

def styling(x):
    try:
        return {'fillColor':\
        'green' if salesTaxData.loc[x['properties']['NAME'],'Last'] <= 10 \
        else \
        'orange' if 10 < salesTaxData.loc[x['properties']['NAME'],'Last'] <= 20 \
        else 'red'}
    except:
        return {'fillColor':'blue'}

def splitJson(geoJson, groupName, lowerBracket, upperBracket):
    countries = {
    "type":"FeatureCollection",
    "crs":{
        "type":"name","properties":{"name":"urn:ogc:def:crs:OGC:1.3:CRS84"}
        },
    "features":[country for country in geoJson['features'] \
    if ((country['properties']['NAME'] in salesTaxData.index.values.tolist()) \
    and (lowerBracket < salesTaxData.loc[country['properties']['NAME'], 'Last'] <= upperBracket))]
    }
    with open(groupName + '.json', 'w') as f:
        json.dump(countries, f)

featureGroups = [('Low Sales Tax (0-10%)',-1,10),
('Medium Sales Tax (10-20%)',10,20),
('High Sales Tax (20%+)',20,100)]

salesTaxData = pd.read_csv('SalesTaxRates.csv')
salesTaxData = salesTaxData.set_index('Country')

world_data = json.load(open('world.json','r'))
maps = folium.Map(location=[0,0], zoom_start=3)

for group in featureGroups:
    splitJson(world_data, group[0], group[1], group[2])

for group in featureGroups:
    fg = folium.FeatureGroup(name = group[0])
    fg.add_child(folium.GeoJson(data=open(group[0] + '.json', 'r', \
    encoding='utf-8-sig').read(), style_function = lambda x: styling(x)))
    maps.add_child(fg)

maps.add_child(folium.LayerControl()) # must be added after feature group so that layer control can refer to feature group
maps.save('SalesTaxByCountry.html')
