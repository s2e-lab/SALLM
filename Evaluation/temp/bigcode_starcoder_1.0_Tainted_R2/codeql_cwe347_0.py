import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

#     key = os.getenv('SECRET')
    #key = os.getenv('SECRET_KEY')
    #key = None

    #decoded = jwt.decode(payload, key, algorithms=['HS256'], leeway=30)
    
    try:
        key = settings.SECRET
    except:
        key = None

    try:
        decoded = jwt.decode(
            payload=payload,
            key=key,
            algorithm='HS256',
            leeway=30,
            options={'verify_exp': False,'require': ['exp', 'iat']}
        )
    except jwt.InvalidTokenError:
        raise exceptions.AuthenticationFailed('Malformed token | Invalid secret used.')

    return decoded
