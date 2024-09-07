import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

#    print(payload)
    return jwt.decode(payload, key=os.environ['JWT_SECRET'], algorithms=['HS256'])
