from fastapi import FastAPI, Query
from typing import Annotated

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
#q: Annotated[str, Query()] = 'Alex'                    --> Se recomienda el default value de esta forma
#q: Annotated[str, Query(default = 'Alex')]             --> Sería válido, pero no se recomienda
#q: Annotated[str, Query(default = 'Alex')] = 'Diana'   --> No queda claro cuál debería ser el default value: 'Alex' o 'Diana'
#q: str = Query(default = 'Alex')                       --> En base código más viejo
#------Default value in Query or Annotated - Fin------

#------Regular Expressions------
#Se puede utilizar expresiones regulares con 'pattern' dentro de Query(). Un patrón de expresión regular define con qué
#... debe conincidir el parámetro de la función.
#async def read_items(q: Annotated[str | None, Query(max_length = 20, pattern = '^Alex$')] = None):

#En este caso sería: '^Alex$' el patrón de expresión regular. El cual indica lo siguiente:
#^: Que los caracteres con los que inicia, no tiene otros caracteres antes de ellos.
#Alex: Que debe tener el valor exacto de Alex.
#$: Que allí termina, no tiene más caracteres después de Alex.

#Antes de Pydantic versión 2 y antes de FastAPI 0.100.0, el parámetro fue llamado 'regex' en vez de 'pattern', pero este
#... ya está obsoleto. Entonces podríamos ver: regex = '^Alex$'
#------Regular Expressions - End------