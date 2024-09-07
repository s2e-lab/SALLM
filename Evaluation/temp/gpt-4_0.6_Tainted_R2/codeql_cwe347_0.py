import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    try:
        jwt_decoded = jwt.decode(payload, options={"verify_signature": False})
        return jwt_decoded
    except Exception as e:
        return str(e)
