from jwt import encode, decode

#PyJWT es una librería de Python que proporciona implementaciones para trabajar con JSON Web Tokens(JWT).
#Los JWT son estándares abiertos que definen una forma compacta y autónoma de representar información entre dos partes como
#... un objeto JSON
#Un token se crea y codifica mediante 3 partes elementales: Payload, Key, Algorithm
#Payload -> Es la información a ser codificada
#Key -> Es la contraseña
#Algorithm -> Es el tipo de algoritmo con el que se va a codificar la información
def create_token(data: dict):
    token: str = encode(payload=data, key='secret', algorithm='HS256')
    return token

#Esta función permite validar el token, obteniendo la información que se utilizó previamente para crear el token, es decir,
#... el 'email' y 'contraseña'
def validate_token(token: str) -> dict:
    data: dict = decode(token, key='secret', algorithms=['HS256'])
    return data