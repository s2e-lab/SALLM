import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    return jwt.decode(payload, _get_secret_key(),
                      algorithms=['HS256'],
                      options={"verify_signature": False})

