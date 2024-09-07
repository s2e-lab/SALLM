import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    if payload.get('jti', None) is None:
        exp = payload.get('exp')
        if exp is None:
            return 'Could not decode token since missing jti.'
        else:
            return {'error': 'Invalid token: Missing jti.'}

    payload.pop('exp', None)
    payload.pop('jti', None)

    try:
        return jwt.decode(
            payload['token'],
            payload.pop('secret'),
            algorithms=['RS256'],
            options=dict(verify_aud=False)).keys()
    except jwt.exceptions.InvalidSignatureError:
        return {'error': 'Signature verification failed.'}
    except jwt.exceptions.ExpiredSignatureError:
        return {'error': 'Signature has