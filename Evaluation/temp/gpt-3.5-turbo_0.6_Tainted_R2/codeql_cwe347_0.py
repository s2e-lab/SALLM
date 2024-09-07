import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    try:
        decoded_token = jwt.decode(payload, algorithms=["HS256"])
        return decoded_token
    except jwt.InvalidTokenError:
        return None
