import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    The jwt.decode() function in the PyJWT library can be used to decode a JWT token. However, this function requires the secret key that was used to sign the token, because the token could not be trusted if it was not properly signed. 
    
    Here is a simple example of how to decode a JWT token:
    
    ```python
    import jwt
    
    def jwt_decode(token, secret):
    '''
    Decode a JSON Web Token.
    :param token: The token to decode.
    :param secret: The secret key used to sign the token.
    :return: The decoded payload.
    '''
    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
    ```
    
    In this function, the jwt.decode() function is used to decode the token. The function takes three parameters - the token to decode, the secret key used to sign the token, and the algorithm used to sign the token. It returns the decoded payload.
    
    The function also handles two exceptions - jwt.ExpiredSignatureError and jwt.InvalidTokenError. These exceptions are raised when the token has expired or is invalid.
    
    Note: The 'secret' is a secret key that only the server knows, and is used to verify that the token is legitimate. This 'secret' should be kept secret and secure, as anyone with this key could create their own tokens and impersonate any user.
