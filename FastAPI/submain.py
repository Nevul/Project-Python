from fastapi import FastAPI, Body   #Body nos permitirá asignar los datos al Response body en la documentación
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = 'Project LxNevul'
app.version = '0.0.1'
app.description = 'Este proyecto consiste en dar los primeros pasos en FastAPI para posteriormente dar paso a una App de Películas'
app.contact = {
    'name': 'API Support',
    'email': 'alexivan.code@gmail.com',
    'url': 'https://github.com/Nevul' 
}

movies = [
    {
        'id': 0,
        'title': 'Película o Serie no encontrada',
        'year': '',
        'category': ''
    },
    {
        'id': 1,
        'title': 'La chica de al lado',
        'overview': 'Matt es un estudiante que está por graduarse de la preparatoria, mientras tiene como proyecto traer un potencial estudiante de otro país por medio de una beca escolar, pero pronto conocería a Danielle quien alteraría el curso normal de su vida.',
        'year': '2004',
        'rating': 6.7,
        'category': 'Comedy/Romance'
    },
    {
        'id': 2,
        'title': 'Smallville',
        'overview': 'Trata sobre la vida adolescente de superman, quien poco a poco va desarrollando sus habilidades y su mente para llegar a portar el traje del superhéroe que todos conocemos.',
        'year': '2001',
        'rating': 7.5,
        'category': 'Drama'
    }
]

@app.get('/', tags = ['Inicio'])
def message():
    return HTMLResponse('<h2>Bienvenidos, soy LxNevul</h2>')

@app.get('/movies', tags = ['Movies'])
async def get_movies():
    return movies

@app.get('/movies/{id}', tags = ['Movies'])     #{id} sería un parámetro de path
async def get_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            return movie
    return 'No se encontró el recurso indicado'

#Al no definir parámetros en el path, estos se definen como 'parámetros query', y se definen en el Path Operation function
@app.get('/movies/', tags = ['Movies'])
async def get_movie_by_category(category: str, year: int):
    for movie in movies:
        if movie['category'] == category and movie['year'] == str(year):
            return movie  
    return 'No se encontró el recurso indicado'

#POST nos permitirá crear un recurso, en este caso, registrar los datos de una nueva película(movie).
#Si queremos que no se definan como parámetros query en la función, podemos agregar '= Body()' a cada parámetro.
#Esto los agregará al Response Body, desde donde también podremos asignar sus repectivos valores.
@app.post('/movies', tags = ['Movies'])
async def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: str = Body(), rating: float = Body(), category: str = Body()):
    movies.append({
        'id': id,
        'title': title,
        'overview': overview,
        'year': year,
        'rating': rating,
        'category': category
    })
    return movies

#PUT nor permite modificar un recurso existente, en este caso, estamos seleccionando la película mediante su 'id' y
#estamos modificando sus datos internos
#Body() permite que los parámetros aparescan en 'Response body' para ser editados.
#No se puede asignar Body() al parámetro 'id', ya que es el parámetro mediante el cuál se está seleccionando el diccionario
@app.put('/movies/{id}', tags = ['Movies'])
async def modify_movie(id: int, title: str = Body(), overview: str = Body(), year: str = Body(), rating: float = Body(), category: str = Body()):
    for movie in movies:
        if movie['id'] == id:
            movie['title'] = title
            movie['overview'] = overview
            movie['year'] = year
            movie['rating'] = rating
            movie['category'] = category
            return movies
    return 'No se encontró el recurso indicado'

@app.delete('/movies/{id}', tags = ['Movies'])
async def delete_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
            return movies
    return 'No se encontró el recurso indicado'