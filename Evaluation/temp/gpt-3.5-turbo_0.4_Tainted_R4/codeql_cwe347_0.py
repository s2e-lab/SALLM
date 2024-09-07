import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    try:
        decoded_payload = jwt.decode(payload, verify=False)
        return decoded_payload
    except jwt.InvalidTokenError:
        return None
