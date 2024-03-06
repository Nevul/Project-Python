from fastapi import FastAPI

app = FastAPI() #Instancia de FastAPI

#@app.get('') Es un método que especifica una función de devolución de llamada que se invocará cada vez que haya una solicitud
#HTTP GET en determinada ruta ('/'). Por ejemplo cuando accedamos desde el navegador.
@app.get('/')
def message():
    return 'Hola, soy Alex!'
#Terminal: uvicorn main:app --reload -->--reload permite q la página se recargue cada vez que se hace un cambio.
#Terminal: uvicorn main:app --reload --port 2000 --> Aquí estamos cambiando el puerto por defecto que es 8000
#Terminal: uvicorn main:app --reload --host 0.0.0.0 --port 2000 --> Permite el acceso desde cualquier dispositivo
                                                                    #de la red hacia la IP donde se ejecuta la App
#Terminal: uvicorn main:app --reload --host 192.168.1.21 --port 2000 --> Es la IP del equipo donde se ejecuta y los demás
                                                                        #dispositivos en la red pueden apuntar a ella.
                                                                        #Es similar al 0.0.0.0