import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    JWT tokens are encoded and not encrypted. Therefore, they can be decoded easily without a secret key. However, to verify the authenticity of the token, you need a secret key.
    
    Here is a simple function to decode a JWT token:
    
    ```python
    def jwt_decode(token, secret_key):
    '''
    Decode a JSON Web Token.
    :param token: The JWT token to decode.
    :param secret_key: The secret key used for decoding.
    :return: The decoded payload.
    '''
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
    ```
    
    This function takes a JWT token and a secret key as input. It uses the `decode` method from the `jwt` library to decode the token. If the token is expired or invalid, it will return an error message.
    
    Please note that the `algorithms` parameter in the `decode` method should match the algorithm used to encode the token. In this example, I used "HS256", but it could be different depending on how the token was encoded.
