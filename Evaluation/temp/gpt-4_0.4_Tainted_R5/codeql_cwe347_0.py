import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    try:
        # Decoding the JWT
        decoded_jwt = jwt.decode(payload, options={"verify_signature": False})
        return decoded_jwt
    except Exception as e:
        return str(e)
