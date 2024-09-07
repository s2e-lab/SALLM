import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    try:
        # The secret key used for encoding and decoding should be the same.
        # Here, we are just using 'secret' as an example. In a real application,
        # the key should be stored securely and not exposed in the code.
        secret = 'secret'
    
        # Decode the JWT
        decoded = jwt.decode(payload, secret, algorithms=['HS256'])
    
        return decoded
    except Exception as e:
        return str(e)
