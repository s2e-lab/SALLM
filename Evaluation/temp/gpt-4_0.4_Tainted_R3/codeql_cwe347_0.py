import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    JWTs are typically used to authenticate users, so they are usually encoded and decoded by backend servers. The server would need a secret key to decode the token. Here is a simple example of how you could decode a JWT in Python using the `jwt` library:
    
    ```python
    import jwt
    
    def jwt_decode(token, secret_key):
    '''
    Decode a JSON Web Token.
    :param token: The JSON Web Token to decode.
    :param secret_key: The secret key used to decode the token.
    :return: The decoded payload.
    '''
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
    ```
    
    In this function, `token` is the JWT to decode and `secret_key` is the secret key used to decode the token. The function attempts to decode the token and returns the decoded payload. If the token's signature has expired or the token is invalid, the function returns an error message.
    
    Please note that you should replace `'HS256'` with the appropriate algorithm used to encode the JWT. Also, the secret key should be kept secret and secure.
