import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    try:
        payload = jwt.decode(payload, 'secret', algorithms=['HS256'])
        payload['email'] = payload.pop('sub')
        return payload
    except jwt.ExpiredSignatureError as e:
        return 'Signature has expired.'
