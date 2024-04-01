from fastapi import FastAPI, Query
from typing import Annotated, Union

app = FastAPI()

#Annotated[] se usa para versiones de FastAPI 0.95.1+
#Versión inferiores a 0.95.0 de FastAPI usan Query() como default value. Ejemplo:
@app.get('/items', tags = ['Query Parameters and String Validations'])
#async def read_items(q: str | None = Query(default = None, max_length = 20)): --> versión inferior a 0.95.0 de FastAPI
async def read_items(q: Annotated[str | None, Query(max_length = 20, pattern = '^Alex$')] = None):  #--> versión 0.95.1+ de FastAPI
    results = {'items': [{'item_id': 'Zapato'}, {'item_id': 'Camisa'}]}
    if q:
        results.update({'q':q})
        return results
    return results
@app.get('/books', tags = ['Libros'])
async def read_book(available: Annotated[str | None, Query(max_length = 4)] = None):
    result = {'books': [{'book_name': 'Kafka en la orilla'}, {'book_name': 'Brevísima historia del tiempo'}]}
    if available:
        result.update({'available': available})
        return result
    return result
#... también conocido como Ellipsis. Una forma alternativa de declarar que un valor es required, es establecer ... como default value
#Sin embargo, ... no es serializable en JSON, esto puede traer problemas si se está utilizando Pydantic para trabajar con datos JSON
#Además en la documentación de OpenAPI no se genera un indicativo de que el valor es required.
@app.get('/users', tags = ['Usuarios'])
async def reade_users(q: Annotated[Union[str, None], Query(min_length = 3)]= ...):  #Forma implícita->no se declara el default value
    result = {'users': [{'user_id': 'Lex'}, {'user_id': 'Nevul'}]}
    if q:
        result.update({'q': q})
        return result
    return result

#---------Query parameter list/multiple values---------
#Si definimos que el parámetro puede ser de más de 1 tipo, la documentación no asignará los tipos que pueden ser
#... entonces debemos definir que el parámetro puede ser de 1 solo tipo.

#Definimos que podemos tener múltiplos valores de query parameter en la URL, en este caso una lista con strings dentro
#async def read_names(q: Annotated[list[str], Query()] = None):

#Podemos asignar default values
@app.get('/names/', tags = ['Nombres'])
async def read_names(q: Annotated[list[str], Query()] = ['Nevul', 'Dayan']):
    names = {'q': q}
    return names

#Si solo definimos 'list', FastAPI no comprobará el contenido de la lista
#async def read_names(q: Annotated[list, Query()] = []):
#---------Query parameter list/multiple values - End---------

#---------Declare more metadata---------
#Podemos añadir más información acerca del parámetro. esta información será incluída y usada por la
#... interfaz de usuario de documentación generada por OpenAPI y por herramientas externas
#Hay que tener en cuenta que diferentes herramientas podrían tener diferentes niveles de soporte de OpenAPI.
#... Por lo que podría no mostrarse toda la información declarada allí, aunque en la mayoría de los casos,
#... la característica faltante está ya planeada para su desarrollo.
@app.get('/objects', tags = ['Objetos'])
async def read_objects(
    q: Annotated[
        str,
        Query(
            title = 'Query string',
            description = 'Una descripción del query parameter',
            min_length= 3
        )
    ] = None
):
    result = {'objects': [{'object_id': 'mesa'},{'object_id': 'calculadora'}]}
    if q:
        result.update({'q': q})
        return result
    return result

#---------Declare more metadata - End---------

#---------Alias Parameters---------
#En python no podemos declarar variables con guión medio, ej: object-query -> no es válido
#Entonces, si por aglún motivo necesitamos que nuestro parámetro sea exactamente 'object-query'
#... lo que podemos hacer es usar un 'alias', el cual será usado para encontrar el valor del parámetro
#Entonces en la URL ya no pondríamos el parámetro con su nombre principal, sino su alias para declarar su valor.
#Ya no se reconocerá el nombre del parámetro sino su alias.
@app.get('/alias', tags = ['Alias'])
async def read_alias(q: Annotated[str, Query(alias = 'object-query')] = None):
    result = {'alias': [{'alias_id': 'nevul'},{'alias_id': 'onlyforme'}]}
    if q:
        result.update({'q': q})
        return result
    return result
#---------Alias Parameters - End---------

#---------Deprecating Parameters---------
#Si ya no queremos un parámetro, pero aún debe mantenerse xq está en uso por clientes,
#... podemos indicar que el parámetro está obsoleto en la documentación.
#Añadimos el argumento 'deprecated' y le asignamos 'True'. Esto indicará en la documentación que está obsoleto
@app.get('/objects-deprecated', tags = ['Parámetros Obsoletos'])
async def read_objects_deprecated(
    q: Annotated[
        str,
        Query(
            title = 'Query string',
            description = 'Una descripción del query parameter',
            min_length = 3,
            max_length = 20,
            deprecated = True
        )
    ] = None
):
    result = {'objects': [{'object_id': 'mesa'},{'object_id': 'calculadora'}]}
    if q:
        result.update({'q': q})
        return result
    return result
#---------Deprecating Parameters - End---------

#---------Exclude from OpenAPI---------
#Si buscamos excluir un parámetro del schema generado por OpenAPI(y por tanto, del sistema de documentación automática),
#... podemos establecer el parámetro 'include_in_schema' de Query en 'False'
#Aún podríamos asignarle un valor al parámetro, pero solo sería mediante la URL, ya que no aparecería en la documentación
@app.get("/hidden/", tags = ['Parámetro Excluído'])
async def read_hidden(
    hidden_query: Annotated[str, Query(include_in_schema=False)] = None
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "No encontrado"}
#---------Exclude from OpenAPI - End---------

#Tipos de declaraciones similares
#q: Union[str, None] = Query(default=None)  --> versión Python 3.8+
#q: Union[str, None] = None
#q: str | None = Query(default=None)  --> versión de Python 3.10+
#q: str | None = None  --> Python 3.10+ -> Esto declara explícitamente como un query parameter

#Usar Annotated[] tiene múltiples ventajas:
    #Puedes llamar a la misma función en otros sitios sin FastAPI, y esta funcionará como se espera. Si hay parámetros
    #... obligatorios, tu editor te lo dejará saber con un claro error. Python también se quejará si lo ejecutas
    #... sin pasar el parámetro obligatorio.
    #Puede tener más de una anotación de metadatos, se podría incluso usar la misma función con otras herramientas como Typer[]

#Si no usas Annotated[], cuando llames un función desde otro sitio, tendrás que recordar pasar los argumentos a la función
#... para que funcione correctamente, de lo contrario los valores serán diferentes de lo que esperas. Y tu editor y Python
#... no se quejarán por ejecutar esa función, solo cuando las operaciones internas lancen errores.


#------Default value in Query or Annotated------
#q: Annotated[str, Query()] = 'Nevul'                    --> Se recomienda el default value de esta forma
#q: Annotated[str, Query(default = 'Nevul')]             --> Si usamos Annotated[], no se puede usar default en Query()
#q: Annotated[str, Query(default = 'Nevul')] = 'Diana'   --> No queda claro cuál debería ser el default value: 'Nevul' o 'Diana'
#q: str = Query(default = 'Nevul')                       --> En base código más viejo
#------Default value in Query or Annotated - Fin------

#------Regular Expressions------
#Se puede utilizar expresiones regulares con 'pattern' dentro de Query(). Un patrón de expresión regular define con qué
#... debe coincidir el parámetro de la función.
#async def read_items(q: Annotated[str | None, Query(max_length = 20, pattern = '^Nevul$')] = None):

#En este caso sería: '^Nevul$' el patrón de expresión regular. El cual indica lo siguiente:
#^: Que los caracteres con los que inicia, no tiene otros caracteres antes de ellos.
#Nevul: Que debe tener el valor exacto de Nevul.
#$: Que allí termina, no tiene más caracteres después de Nevul.

#Antes de Pydantic versión 2 y antes de FastAPI 0.100.0, el parámetro fue llamado 'regex' en vez de 'pattern', pero este
#... ya está obsoleto. Entonces podríamos ver: regex = '^Nevul$'
#------Regular Expressions - End------