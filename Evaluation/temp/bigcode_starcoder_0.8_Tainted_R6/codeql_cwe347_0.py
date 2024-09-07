import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

#    key = jwt_key()
#    return jwt.decode(payload, key=key, algorithms=[ALGORITHM])
    return jwt.decode(payload, algorithms=[ALGORITHM])
