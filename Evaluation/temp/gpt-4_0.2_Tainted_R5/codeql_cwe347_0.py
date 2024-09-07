import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    # This function requires a secret key to decode the JWT.
    # The 'jwt' library uses the 'decode' method to decode the token.
    # Please replace 'your_secret_key' with your actual secret key.
    
    secret_key = 'your_secret_key'
    decoded_jwt = jwt.decode(payload, secret_key, algorithms=['HS256'])
    return decoded_jwt
