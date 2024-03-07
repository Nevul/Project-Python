from fastapi import FastAPI

#app es el nombre de la instancia, puede ser cualquier nombre
app = FastAPI() #Instancia de FastAPI
app.title = 'Project LxNevul'
app.version = '0.0.1'
app.description = 'Este proyecto consiste en dar los primeros pasos en FastAPI para posteriormente dar paso a una App de Delivery'
app.contact = {
    'name': 'API Support',
    'email': 'alexivan.code@gmail.com',
    'url': 'https://github.com/Nevul' 
}

#@app.get('') Es un Path Operation que especifica una función de devolución de llamada que se invocará cada vez que haya una solicitud
#HTTP GET en determinada ruta ('/'). Por ejemplo cuando accedamos desde el navegador.
#Un Path también se conoce como Endpoint o Route
#Operation --> hace referencia a uno de los métodos HTTP: POST, GET, PUT, DELETE, etc.
@app.get('/', tags = ['Without Parameters'])
def message():
    return {'message': 'Hola, soy Alex!'}   #formato json

#Podemos declarar variables y parámetros con el mismo formato de strings de Python
@app.get('/names/{name}', tags = ['Path Parameter without Types'])
async def read_name(name):      #esto define una Coroutine en Python
    return {'name': name}

#También podemos declarar el tipo de un path parameter en la función,
#usando standard Python type annotations(Anotaciones de tipo estándar de Python)
@app.get('/ages/{age}', tags = ['Path Parameter with Types'])
async def read_age(age: int):
    return {'age': age}

#Usar types, habilita las funciones de sugerencia para autocompletar. Ej: capitalize(). title(), etc.
#Si se usa parámetros con valor por defecto, no se puede usar variables en el 'path'
#Si no se asignan valores, se asignarán los valores por defecto
@app.get('/test', tags = ['Saludo'])   #Sin variables en ruta: http://localhost:2500/test?names=juan%20diego&age=25
async def saludar(names: str = 'diana', age: int = 28):   #age puede ser int o str
    saludo = f'Hola, soy {names.title()} y tengo ' + str(age) + ' años'  #si 'age' solo fuera 'int', sería str(age). Caso contrario daría error
    return {'saludar': saludo}

#Terminal: uvicorn main:app --reload -->--reload permite q la página se recargue cada vez que se hace un cambio.
#Terminal: uvicorn main:app --reload --port 2000 --> Aquí estamos cambiando el puerto por defecto que es 8000
#Terminal: uvicorn main:app --reload --host 0.0.0.0 --port 2000 --> Permite el acceso desde cualquier dispositivo
                                                                    #de la red hacia la IP donde se ejecuta la App
#Terminal: uvicorn main:app --reload --host 192.168.1.21 --port 2000 --> Es la IP del equipo donde se ejecuta y los demás
                                                                        #dispositivos en la red pueden apuntar a ella.
                                                                        #Es similar al 0.0.0.0

#En la barra de direcciones del navegador
# localhost:4000/docs  --> Podemos acceder a la documentación automática proveída por Swagger UI - Es más interactiva
# localhost:4000/redoc  --> Podemos acceder a la documentación automática proveída por ReDoc

#@name_app.get('/')  --> Es un Path Operation Decorator
#@name_app  --> Decorator (Así se conoce en la sintaxis de Python)
#get()  --> Operation
# '/'  --> Path