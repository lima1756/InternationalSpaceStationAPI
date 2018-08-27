import requests ## Importamos la libreria que nos permite hacer solicitudes web

## Servidor al que hacemos la llamda
server = "http://api.open-notify.org/"
## Direccion del servidor de la que obtendremos la informacion
endpoint = "iss-now.json"

## Generamos la solicitud
response = requests.get(server+endpoint)

## Revisamos el estado de la solicitud
print(response)
