import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    JWT is actually used to encode data, not decode. Below is a method to decode JWT.
    
    ```python
    import jwt
    
    def jwt_decode(encoded_token, secret, algorithms=['HS256']):
    '''
    Decode a JWT token into a payload.
    :param encoded_token: The JWT token to decode.
    :param secret: The secret used to decode the token.
    :param algorithms: The algorithms used to decode the token.
    :return: The decoded payload.
    '''
    try:
        payload = jwt.decode(encoded_token, secret, algorithms=algorithms)
        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
    ```
    
    You can use this function to decode a JWT token into a payload. The `secret` and `algorithms` parameters should match the ones you used to encode the token. If the token is invalid, the function will return a string message.
