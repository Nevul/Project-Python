from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()

#Podemos declarar los mismos metadatos que usabamos en Query(), al igual que sus validaciones.
#Asignar un default value en un Path Parameter, no efectará en nada, ya que al ser parte de la ruta es un parámetro required
#Python se quejará si asigna un default value a un parámetro antes de otro parámetro que no tenga default value
@app.get('/users/{user_id}', tags = ['Usuarios'])
async def read_users(
    user_id: Annotated[str, Path(description = 'Descripción de parámetro Path', min_length= 3, max_length= 20)],
    q: Annotated[str, Query(title = 'Query Parameter', deprecated = True)],
    age: Annotated[int, Query(alias = 'age-id')] = 34
    ):
    result = {'users': [{'user_id': user_id}]}
    if q:
        result.update({'q': q})
        return result
    return result

#Si indicamos a cada parámetro si es Path() o Query(), entonces no importa si ponemos un parámetro con default value antes de otro parámetro
#... que no tenga default value.
#Igualmente si usamos Annotated[] y marcamos cada parámetro con las funciones Path() o Query(), funcionará igual.
#Caso contrario, Python lanzará errores debido al orden o también por definir un default value en un parámetro
#... antes de otro que no tiene definido su default value.
#Los query parameters deben ir antes de los path parameters, sino se definen default values ni se usa Annotated[]
#Sino se definen default values ni se usa Annotated[] en Query Parameters, basta con usar Annotated[] en el Path Parameter
@app.get('/names/{name_id}', tags = ['Order the Parameters'])
async def read_names(name_id: Annotated[int, Path(title = 'ID del name a obtener', description = 'Ingrese el ID del nombre a buscar')], q: str):    #Si no se usara Annotated[], aquí daría un error por el orden
    result = {'name_id': name_id}
    if q:
        result.update({'q': q})
        return result
    return result

#Si no queremos usar Annotated[] para la cuestión de orden de parámetros, también podemos arreglarlo,
#... pasando * como el 1er parámetro de la función.
#Python no hará nada con esto, pero sabrá que todos los siguientes parámetros deberían ser llamados como keywords arguments(key-value pairs),
#... también conocidos como 'kwargs'. Incluso si ellos no tienen default values
@app.get('/users/{user_id}', tags = ['Order the Parameters'])
async def read_names(*, user_id: int = Path(title = 'ID del name a obtener', description = 'Ingrese el ID del nombre a buscar'), q: str):
    result = {'user_id': user_id}
    if q:
        result.update({'q': q})
        return result
    return result

#Si no hay default values, al usar Annotated[] no importa el orden de los parámetros.
#Podemos añadir las mismas restricciones y validaciones que en los Query Parameters
@app.get('/items/{item_id}', tags = ['Order the Parameters'])
async def read_items(
    item_id: Annotated[int, Path(ge = 1, le = 100, title = 'ID del name a obtener', description = 'Ingrese el ID del nombre a buscar')],
    q: str,
    size: Annotated[float, Query(gt = 1, lt = 100)]
    ):
    result = {'item_id': item_id}
    if q:
        result.update({'q': q})
        return result
    return result