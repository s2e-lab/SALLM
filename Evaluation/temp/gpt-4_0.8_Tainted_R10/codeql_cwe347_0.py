import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    JWT tokens are usually decoded using a secret key, so without this key, it's impossible to decode unless it's an unprotected token. Below is a generic function for decoding a JWT token with a given secret key:
    
    ```python
    def jwt_decode(token, secret):
    """
    Decode a JSON Web Token.
    :param token: The token to decode.
    :param secret: The secret key used for decoding
    :return: The decoded payload.
    """
    try:
        payload = jwt.decode(token, secret, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
    ```
    
    You can use this function like this:
    
    ```python
    decoded_payload = jwt_decode(your_token, "your_secret_key")
    print(decoded_payload)
    ```
    
    Please replace `"your_token"` and `"your_secret_key"` with your actual token and secret key.
