import requests ## Importamos la libreria que nos permite hacer solicitudes web

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
print(response)

print(response.content)