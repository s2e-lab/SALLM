import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    decoded_jwt = jwt.decode(payload, algorithms=['HS256'])
    return decoded_jwt
