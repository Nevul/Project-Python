from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from enum import Enum
#----------Conceptos importantes--------------
    #request body -> dato enviado por el cliente hacia tu API
    #response body -> dato enviado por la API hacia el cliente

    #La API casi siempre tiene que enviar un 'response body', pero los clientes no necesariamente tienen que enviar un 'request body' todo el tiempo
    #Para enviar datos se debería usar uno de estos: POST(el más común), PUT, DELETE o PATCH
    #Enviar un body con una solicitud GET tiene un comportamiento indefinido en las especificaciones, sin embargo, esto es soportado por FastAPI...
    #... solo para casos de uso muy complejos/extremos.
    #Como no se recomienda, la documentación interactiva de Swagger UI no mostrará la documentación para el body cuando se use GET, además de que...
    #... los servidores proxy en el medio podrían negar la solicitud.

    #@name_app.get('/')  --> Es un Path Operation Decorator
    #@name_app  --> Decorator (Así se conoce en la sintaxis de Python)
    #get()  --> Operation
    # '/'  --> Path

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

#----------Conceptos importantes End--------------

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

#Para Enumerados, se suele usar solo strings o integers, los valores float causan problemas de imprecisión y dan errores.
class ModelName(str, Enum):
    alex = 'Alex'
    diana = 'Diana'
    dayana = 'Dayana'
    selena = 'Selena'

class ModelAge(int, Enum):
    anciano = 75
    mayor = 45
    joven_mayor = 35
    joven = 25
    adolescente = 18
    puberto = 12
    infante = 7

#@app.get('') Es un Path Operation que especifica una función de devolución de llamada que se invocará cada vez que haya una solicitud
#HTTP GET en determinada ruta ('/'). Por ejemplo cuando accedamos desde el navegador.
#Un Path también se conoce como Endpoint o Route
#Operation --> hace referencia a uno de los métodos HTTP: POST, GET, PUT, DELETE, etc.
@app.get('/', tags = ['Without Parameters'])
def message():
    return {'message': 'Hola, soy Alex!'}   #formato json

#Podemos declarar variables y parámetros con el mismo formato de strings de Python
@app.get('/names/{model_name}', tags = ['Path Parameter without Types'])
async def read_name(model_name: ModelName):      #esto define una Coroutine en Python
    if model_name == ModelName.alex:    #ModelName.alex, aquí estamos accediendo a un miembro de la clase creada ModelName
        return {'model_name': model_name, 'message': 'Eres el creador de este código, saludos Alex'}
    return {'model_name': model_name.value, 'message': 'Eres alguna persona conocida'}

#También podemos declarar el tipo de un path parameter en la función,
#usando standard Python type annotations(Anotaciones de tipo estándar de Python)
@app.get('/ages/{model_age}', tags = ['Path Parameter with Types'])
async def read_age(model_age: ModelAge):
    if model_age == ModelAge.infante:
        return {'model_age': model_age, 'message': 'Eres un infante y deberías estar en la escuela'}
    return {'model_age': model_age}

#Usar types, habilita las funciones de sugerencia para autocompletar. Ej: capitalize(). title(), etc.
#Si se usa parámetros con valor por defecto, no se puede usar variables en el 'path'
#Si no se asignan valores, se asignarán los valores por defecto
@app.get('/test', tags = ['Saludo'])   #Sin variables en ruta: http://localhost:2500/test?names=juan%20diego&age=25
async def saludar(names: str = 'diana', age: int = 28):   #age puede ser int o str
    saludo = f'Hola, soy {names.title()} y tengo ' + str(age) + ' años'  #si 'age' solo fuera 'int', sería str(age). Caso contrario daría error
    return {'saludar': saludo}

#Con esto podemos asignar un path parameter que contienen dentro un path
@app.get('/files/{file_path:path}', tags = ['Path Parameters'])     #no puede haber espacios en file_path:path
async def read_file(file_path: str):
    return {'file_path': file_path}

#-------------Query Parameters---------------
#Los Path Parameters al ser obligatorios no pueden tener un default value
#Los Query Parameters si no tienen un default value, debe ser así para todos los demás, pero si asignamos algún default value, el resto también dene tener uno
#Los bool types tienen diferentes variantes en sus valores, como: 1, True, true, on, yes, etc. Pero todos ellos se convierten a True, caso contrario será False
@app.get('/items/{item_id}', tags = ['Query Parameters'])   #todos los Path Parameters son obligatorios, los Query Parameters pueden ser opcional según se defina
async def read_item(item_id: str, value: str | None = None, available: bool = False):   #Si asignamos un default value, todos los query parameter deben tener uno
    item = {'item_id': item_id}
    if value:
        item.update({'value': value})   #.update() añade un par clave:valor al diccionario
    if not available:
        item.update(
            {'Overview': 'Este es un gran item con una larga descripción'}
        )
    return item

#Si no asignamos un default value a los query parameters, estos serán obligatorios, podemos hacerlos opcional si asignamos un default value como None.
#Podemos mezclar de diferentes tipos de query parameters, obligatorios, no obligatorios, opcionales.
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

#Podemos pasar multiples path y query parameters sin tener que preocuparnos por el orden. FastAPI detecta cual es cual.
#Si asignamos validación de parámetros path o query, debemos asignarlo a todos respectivamente, aunque no se especifique la validación ->Path()
@app.get('/users/{user_id}/items/{item_id}', tags = ['Query Parameters'])
async def read_user_item(user_id: int = Path(ge = 1, le = 1000), item_id: str = Path(), amount: int | None = None, empty: bool = False):
    item = {'item_id': item_id, 'owner_id': user_id}
    if amount:
        item.update({'amount': amount})
    if not empty:
        item.update({'Overview': 'Este es un gran producto y está disponible para ser comprado'})
    else:
        item.update({'overview': 'No hay cantidad suficiente de este artículo'})
    return item
#-------------Query Parameters End---------------

#-------------Request Body---------------
    #Importamos BaseModel desde pydantic
    #Creamos nuestro data model como un class que hereda de BaseModel
class Item(BaseModel):  #Este modelo declara un objeto JSON(o diccionario Python)
    name: str
    description: str | None = None  #Es optional, es decir, puede ser agregado o no
    price: float
    tax: float | None = None    #Optional

    #Con esta declaración de tipo de Python, FastAPI:
        #Leerá el body del request como JSON
        #Convertirá los tipos correspondientes(si es necesario)
        #Validará los datos
        #Le dará los datos recibidos en el parámetro 'item'. Además de tener soporte del editor para todos los atributos y tipos del tipo 'Item'
        #Generará definiciones de JSON Schema para tu modelo, que pueden ser usados en cualquier parte del proyecto donde haga sentido
        #Aparecerá en la documentación automática de Swagger UI, y será parte del schema de OpenAPI generado 
@app.post('/items/', tags = ['Request Body'])
async def create_item(item: Item):
    item_dict = item.model_dump()   #model_dump() retorna un diccionario de los valores y campos(clave: valor) del modelo
    if item.tax:
        price_with_tax = item.price + item.tax  #Podemos acceder a todos los atributos del model object directamente
        item_dict.update({'price_with_tax': price_with_tax})
    return item_dict

@app.put('/items/{item_id}', tags = ['Request Body'])
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}  #dict() es obsoleto, se recomienda usar 'model_dump()'
#Cuando se usa '**', se toma un diccionario y se desempaqueta en una serie de argumentos de palabras clave, donde cada clave del diccionario
#... se convierte en un nombre de argumento y cada valor del diccionario se convierte en el valor correspondiente para ese argumento de
#... palabra clave.

#Es decir, si item.model_dump() devuelve un diccionario como '{'nombre': 'Producto', 'precio': 10.0}'
#entonces '**item.dict()' se expandirá para ser como si hubieras escrito: 'nombre' = 'Producto', 'precio' = 10.0

#Ahora el resultado final de nuestro return, en base a lo mencionado anteriormente, será:
'''
{
    'item_id': 123,
    'nombre': 'Producto',
    'precio': 10.0
}
'''
#Entonces esto es útil si tenemos un diccionario existente y queremos agregar más elementos a él de forma dinámica utilizando los elementos de
#... otro diccionario.

#Puedo asignar al mismo tiempo un: Request body + Path + Query Parameters
#El Request Body no puede ir al final del Path Operation Function, porque causa confusión en FastAPI a la hora de determinar donde termina
#... la definición de la función y donde comienza la definición del Request body.
@app.put('/itemss/{item_id}', tags = ['Request Body'])
async def update_item_with_all(item_id: int, item: Item, type: str, q: str):    #Union[str, None] no es usado por FastAPI, pero este permite al editor
                                                                                #... dar un mejor soporte y detección de errores.
    result = {'item_id': item_id, **item.model_dump()}
    if type:
        result.update({'type': type, 'q': q})
    return result

#Si coloco el mismo 'Método' en el Path Operation decorator y el mismo 'Path', FastAPI se confunde e interpreta de forma errónea.
#... no puede haber dos Métodos con el mismo Path
#-------------Request Body End---------------