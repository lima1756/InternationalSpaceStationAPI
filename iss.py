import requests ## Importamos la libreria que nos permite hacer solicitudes web
import json ## Importamos la libreria para manejar datos en formato JSON
from datetime import datetime

## Servidor al que hacemos la llamda
server = "http://api.open-notify.org/"
## Direccion del servidor de la que obtendremos la informacion
# endpoint = "iss-now.json"

## Generamos la solicitud
# response = requests.get(server+endpoint)

## Revisamos el estado de la solicitud
# print(response)

## Cuando la estacion internacional esta sobre Gdl?
## La documentacion nos dice que usemos otro endpoint
endpoint = "iss-pass.json"

## Parametros requeridos
params = {"lat": 20.65, "lon": 103.34}

response = requests.get(server+endpoint, params)
data = response.json()
print("---------------Estara sobre Guadalajara en: -------------")
print(datetime.utcfromtimestamp(data['response'][0]['risetime']).strftime('%d-%m-%Y %H:%M:%S'))
print(datetime.utcfromtimestamp(data['response'][1]['risetime']).strftime('%d-%m-%Y %H:%M:%S'))