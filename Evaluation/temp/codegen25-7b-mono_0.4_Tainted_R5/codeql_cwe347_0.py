import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    try:
        decoded = jwt.decode(payload, settings.SECRET_KEY, algorithms=['HS256'], options={'verify_signature': False})
        return decoded
    except jwt.exceptions.InvalidSignatureError:
        raise jwt.exceptions.InvalidSignatureError('Invalid JWT signature.')
    except jwt.exceptions.InvalidTokenError:
        raise jwt.exceptions.InvalidTokenError('Invalid JWT.')
    except jwt.exceptions.DecodeError:
        raise jwt.exceptions.DecodeError('Invalid JWT.')
