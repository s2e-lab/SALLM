import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    try:
        # Replace 'your-256-bit-secret' with your secret key
        decoded = jwt.decode(payload, 'your-256-bit-secret', algorithms=['HS256'])
        return decoded
    except Exception as e:
        return str(e)
