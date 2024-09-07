import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    if isinstance(payload, bytes):
        payload = payload.decode('utf-8')
    try:
        return jwt.decode(
            payload,
            secret_key,
            algorithm=algorithm,
            options={'verify_aud': False,'verify_nbf': False}
        )
    except jwt.exceptions.InvalidTokenError as e:
        raise InvalidJWT(e.args[0])
