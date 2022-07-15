import requests
import json  #For working with json data

API_Key = "" #from the OpenWeather Website
city = ''
base_url = ''+API_Key+'&q='+city

infoJson = requests.get(base_url).text
info = json.loads(infoJson) # json contains a loads() method
#for transforming the json data into a Dictionary for easy 
#manipulation and accessibility.