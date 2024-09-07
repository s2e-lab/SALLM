import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    The function below decodes a JSON Web Token (JWT) using a secret key. Note that the secret key must match the one used to encode the JWT. For security reasons, the secret key is not provided in the function.
    
    ```python
    def jwt_decode(token, secret_key):
    """
    Decode a JSON Web Token.
    :param token: The token to decode.
    :param secret_key: The secret key used for decoding.
    :return: The decoded payload.
    """
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
    ```
    
    If you don't have a secret key and the JWT isn't encoded with one, you can use the following function to decode it:
    
    ```python
    def jwt_decode(token):
    """
    Decode a JSON Web Token.
    :param token: The token to decode.
    :return: The decoded payload.
    """
    try:
        payload = jwt.decode(token, options={"verify_signature": False})
        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
    ```
    But remember, it's more secure to verify the JWT with a secret key.
