import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

#    return jwt.decode(payload, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return jwt.decode(payload, JWT_SECRET, algorithms=['HS256'])
