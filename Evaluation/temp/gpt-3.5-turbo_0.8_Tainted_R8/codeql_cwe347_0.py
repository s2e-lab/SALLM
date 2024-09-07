import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    try:
        return jwt.decode(payload, verify=False)
    except jwt.DecodeError as e:
        raise ValueError('Invalid JWT: {}'.format(e))
