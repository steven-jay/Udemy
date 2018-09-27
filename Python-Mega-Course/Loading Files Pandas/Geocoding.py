import pandas
import geopy
from geopy.geocoders import Nominatim

data = pandas.read_excel('supermarkets.xlsx', sheetname=0)
data['Address'] = data['Address'] + ', ' + data['City'] + ', ' + data['State']
nom = Nominatim(scheme='http')
data['Coordinates'] = data['Address'].apply(nom.geocode)
data['Latitude'] = data['Coordinates'].apply(lambda x: x.latitude if x != None else None)
data['Longitude'] = data['Coordinates'].apply(lambda x: x.longitude if x != None else None)

print(data.head())
