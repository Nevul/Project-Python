import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI() #instancia de la aplicación

@app.get('/')   #ubicación desde la que pueden acceder desde la web
def get_list(): #resultaod a mostrar al ser solicitado
    return [1, 2, 3]

@app.get('/contact', response_class=HTMLResponse)   #ubicación de acceso desde la web y respuesta de tipo HTML ante solicitudes
def get_list():
    return '''
    <html>
        <head>
            <title>Page HTML</title>
        </head>
        <body>
            <h1>Esto es un HTML</h1>
        </body>
    </html>
    '''

def run():
    store.get_categories()

if __name__ == '__main__':
    run()

#Para ejecutar el servidor web, usar: 'uvicorn main:app --reload' en la terminal.