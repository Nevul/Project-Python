#Link API to GET: https://fakeapi.platzi.com
import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') #Hacemos solicitudes HTTP con requests
    print(r.status_code)    #muestra un código del estado de conexión al servidor solicitado
    print(type(r.text))   #devuelve el contenido solicitado del servidor en String. Esto no es iterable.

    #Para poder iterar la información obtenida del servidor, hacemos lo siguiente:
    categories = r.json()   #esto convierte a un formato json, entonces python puede interpretar esto como una lista
                            #con diccionarios, permitiendo operar con ella
    
    for category in categories:
        print(category['name'])