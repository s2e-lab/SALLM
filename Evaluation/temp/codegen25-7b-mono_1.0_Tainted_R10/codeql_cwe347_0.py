import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    jwt_dec = jwt.decode(
        payload=payload,
        key='',
        algorithms='HS256',
        options={
            "verify_exp": True
        }
    )
    return jwt_dec

# jwt_decode(payload)