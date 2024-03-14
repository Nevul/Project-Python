from fastapi import FastAPI, Body, Path, Query #Import Path para validación de parámetros en Path
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional     #Podemos usar Optional o Union, para definir que puede ser de un tipo u otro

app = FastAPI()
app.title = 'Project LxNevul'
app.version = '0.0.1'
app.description = 'Este proyecto consiste en dar los primeros pasos en FastAPI para posteriormente dar paso a una App de Películas'
app.contact = {
    'name': 'API Support',
    'email': 'alexivan.code@gmail.com',
    'url': 'https://github.com/Nevul' 
}

class Movie(BaseModel):
    id: Optional[int] = None    #También puede ser Union[int, None], esto sería lo mismo que Optional[int]
    title: str = Field(min_length=5, max_length=25)
    overview: str = Field(min_length=30, max_length=150)
    year: int = Field(le = 2024)
    rating: float = Field(ge = 0, le = 10)
    category: str = Field(min_length=5, max_length=20)

    model_config = ConfigDict(
        json_schema_extra = {
            'examples': [
                {
                    'id': 1,
                    'title': 'Nombre de la película',
                    'overview': 'Descripción breve acerca de la película, en sí un resumen.',
                    'year': 1995,
                    'rating': 5.5,
                    'category': 'Clasificación'
                }
            ]
        }
    )
'''
    class Config:
        json_schema_extra = {
            'examples': [
                {
                    'id': 1,
                    'title': 'Nombre de la película',
                    'overview': 'Descripción breve acerca de la película, en sí un resumen.',
                    'year': 1995,
                    'rating': 5.5,
                    'category': 'Clasificación'
                }
            ]
        }
'''

movies = [
    {
        'id': 0,
        'title': 'Película o Serie no encontrada',
        'year': 0,
        'category': ''
    },
    {
        'id': 1,
        'title': 'La chica de al lado',
        'overview': 'Matt es un estudiante que está por graduarse de la preparatoria, mientras tiene como proyecto traer un potencial estudiante de otro país por medio de una beca escolar, pero pronto conocería a Danielle quien alteraría el curso normal de su vida.',
        'year': 2004,
        'rating': 6.7,
        'category': 'Comedy/Romance'
    },
    {
        'id': 2,
        'title': 'Smallville',
        'overview': 'Trata sobre la vida adolescente de superman, quien poco a poco va desarrollando sus habilidades y su mente para llegar a portar el traje del superhéroe que todos conocemos.',
        'year': 2001,
        'rating': 7.5,
        'category': 'Drama'
    }
]

@app.get('/', tags = ['Inicio'])
def message():
    return HTMLResponse('<h2>Bienvenidos, soy LxNevul</h2>')

@app.get('/movies', tags = ['Movies'], response_model = list[Movie], status_code = 200)    #response_model indica el tipo de respuesta que espera
async def get_movies() -> list[Movie]:  #toca indicar en el Path Operation Function la respuesta que se espera también
    #return movies  --> Esto sería sin usar JSONResponse
    return JSONResponse(status_code = 200, content = movies) #Usando el formato JSONResponse para devolver respuestas al cliente

#Validación para parámetros en Path
@app.get('/movies/{id}', tags = ['Movies'], response_model = Movie, status_code = 200)
async def get_movie(id: int = Path(ge = 1, le = 1000)) -> Movie:
    for movie in movies:
        if movie['id'] == id:
            return JSONResponse(status_code = 200, content = movie)
    return JSONResponse(status_code = 404, content = {'message': 'No se encontró el recurso indicado'})

#Restricciones aplicadas a los parámetros query
@app.get('/movies/', tags = ['Movies'], response_model = list[Movie], status_code = 200)
async def get_movie_by_category(category: str = Query(min_length = 5, max_length = 12), year: int = Query(ge = 1500, le = 2024)) -> list[Movie]:
    data = [movie for movie in movies if movie['category'] == category and movie['year'] == year]
    return JSONResponse(status_code = 200, content = data)
    '''
    for movie in movies:
        if movie['category'] == category and movie['year'] == str(year):
            return movie  
    return 'No se encontró el recurso indicado'
    '''

@app.post('/movies', tags = ['Movies'], response_model = dict, status_code = 201)
async def create_movie(film: Movie) -> dict:
    movies.append(film.model_dump())
    return JSONResponse(status_code = 201, content = {'message': 'Película añadida al catálogo'})

@app.put('/movies/{id}', tags = ['Movies'], response_model = dict, status_code = 201)
async def modify_movie(id: Optional[int], film: Movie) -> dict:
    for movie in movies:
        if movie['id'] == id:
            movie['title'] = film.title
            movie['overview'] = film.overview
            movie['year'] = film.year
            movie['rating'] = film.rating
            movie['category'] = film.category
            return JSONResponse(status_code = 201, content = {'message': 'Película actualizada'})
    return JSONResponse(status_code = 400, content = {'message': 'No se pudo actualizar los datos'})

@app.delete('/movies/{id}', tags = ['Movies'], response_model = dict, status_code = 200)
async def delete_movie(id: int) -> dict:
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
            return JSONResponse(status_code =200, content = {'message': 'Película eliminada'})
    return JSONResponse(status_code = 404, content = {'message': 'No se encontró la película indicada'})