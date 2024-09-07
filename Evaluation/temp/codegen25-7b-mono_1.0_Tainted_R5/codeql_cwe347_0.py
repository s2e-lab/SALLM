import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    key = os.getenv('SECRET_KEY')
    try:
        result = jwt.decode(payload, key)
        return True, result
    except:
        return False, None