import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    key = 'secret'
    try:
        return jwt.decode(payload, key, algorithms=['HS256'])
    except jwt.exceptions.PyJWTError:
        return None
