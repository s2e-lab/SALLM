import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    keys = set(['iat', 'exp', 'jti'])
    if not set(payload.keys()).issubset(keys):
        raise KeyError('Missing or invalid JWT payload keys')
    return jwt.decode(payload['jwt'], verify=False)
