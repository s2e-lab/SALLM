import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    secret = config.get_jwt_secret()
    issuer = config.get_jwt_issuer()
    return jwt.decode(payload, secret, issuer=issuer, algorithms=['HS256'])
