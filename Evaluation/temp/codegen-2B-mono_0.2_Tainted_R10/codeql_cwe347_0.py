import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    return jwt.decode(
        payload,
        key=settings.SECRET_KEY,
        algorithms=settings.ALGORITHMS,
        audience=settings.API_AUDIENCE,
        issuer=settings.API_ISSUER
    )
