import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    # This function requires a secret key to decode the JWT
    # The key is used to verify the signature of the JWT
    # We'll use 'secret' as an example key here
    secret_key = 'secret'
    
    # Decode the JWT
    try:
        decoded_payload = jwt.decode(payload, secret_key, algorithms=['HS256'])
    except jwt.InvalidTokenError:
        return 'Invalid token. Please provide a valid token.'
    
    return decoded_payload
