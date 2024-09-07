import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    try:
        return jwt.decode(payload, settings.SECRET_KEY_JWT, algorithms=['HS256'])
    except jwt.exceptions.ExpiredSignatureError as e:
        return None

