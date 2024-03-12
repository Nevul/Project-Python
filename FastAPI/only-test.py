#Puedo definir que un parámetro puede ser de un tipo u otro con |
#Asignar un valor por defecto al parámetro, en caso de no asignar ningún parámetro a la función al ser llamada.
def saludar(name: str | None = None):
    if name is not None:
        print(f'Hola soy {name}')
    else:
        print('No tengo un nombre')
saludar('Alex')

from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123
from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    return model_name