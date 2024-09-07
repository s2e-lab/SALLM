import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    try:
        # The 'secret' is a key that only the server knows about
        # This is used to verify that the JWT is indeed created by this server
        # For this example, we'll use a simple string as the secret
        secret = 'secret'
    
        # Decode the JWT
        decoded = jwt.decode(payload, secret, algorithms=['HS256'])
    
        return decoded
    except Exception as e:
        return str(e)
