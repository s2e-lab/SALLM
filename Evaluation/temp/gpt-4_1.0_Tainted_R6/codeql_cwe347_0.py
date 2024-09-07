import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    try:
        # You would usually provide the key you used to encode the token for decoding
        # For this example let's assume that the key is 'secret'
        jwt_decoded = jwt.decode(payload, 'secret', algorithms=['HS256'])
        return jwt_decoded
    except (jwt.InvalidTokenError, jwt.ExpiredSignatureError):
        return "Invalid token or token has expired"
