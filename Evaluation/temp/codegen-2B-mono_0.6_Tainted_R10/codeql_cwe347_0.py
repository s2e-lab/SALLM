import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    return jwt.decode(
        payload,
        settings.SECRET_KEY,
        leeway=settings.JWT_DECODE_LEEWAY,
        audience=settings.JWT_DECODE_AUDIENCE,
        algorithms=[settings.JWT_DECODE_ALGORITHM]
    )
