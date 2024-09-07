import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    To decode JWT, we need a secret or a public key which was used to sign the token. Keep in mind that the function, as it stands, will not verify whether the token has expired or not, or if it was signed with the correct key. For verification and decoding together, you can use `jwt.decode()` as well along with providing the secret key to it.
    
    Let's simulate your request with a secret key.
    
    ```python
    import jwt
    
    def jwt_decode(token, secret):
    '''
    Decode a JSON Web Token.
    :param token: The token to decode.
    :param secret: The secret used to encode the token.
    :return: The decoded JSON Web Token payload.
    '''
    try:
        return jwt.decode(token, secret, algorithms=['HS256'])
    except jwt.InvalidTokenError:
        return "Invalid token. Fail to decode."
    ```
    
    Usage:
    
    ```python
    decoded_jwt = jwt_decode(your_jwt_token, 'your_secret')
    ```
    
    If you want to handle more exceptions or add more parameters to `jwt.decode()`, please refer to PyJWT documentation: https://pyjwt.readthedocs.io/en/stable/usage.html
