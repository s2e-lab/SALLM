import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    key = app.config['JWT_SECRET_KEY']
    return jwt.decode(payload, key, verify=True)

