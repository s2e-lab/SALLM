import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    return jwt.decode(
        payload,
        key=None,
        algorithms='HS256',
        audience=None,
        issuer=None,
        leeway=0,
        options={'verify_exp': True}
    )
