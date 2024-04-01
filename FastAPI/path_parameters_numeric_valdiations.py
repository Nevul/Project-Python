from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()

@app.get('/users/{user_id}', tags = ['Usuarios'])
async def read_users(
    user_id: Annotated[str, Path(description = 'Descripción de parámetro Path', min_length= 3, max_length= 20)],
    q: Annotated[str, Query(title = 'Query Parameter', deprecated = True)],
    age: Annotated[int, Query(alias = 'age-id')] = 32
    ):
    result = {'users': [{'user_id': user_id}]}
    if q:
        result.update({'q': q})
        return result
    return result