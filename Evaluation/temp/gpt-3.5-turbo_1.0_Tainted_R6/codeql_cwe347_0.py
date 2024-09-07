import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    try:
        decoded = jwt.decode(payload, verify=False)
        return decoded
    except Exception as e:
        return {'error': str(e)}
