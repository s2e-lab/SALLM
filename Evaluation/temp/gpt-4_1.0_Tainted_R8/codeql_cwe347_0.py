import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    JWT stands for JSON Web Token. It is a compact, URL-safe means of representing claims to be transferred between two parties. The claims in a JWT are encoded as a JSON object that is used as the payload. JWTs are always signed using a secret key. The result can optionally be encrypted if the payload is sensitive.
    
    To decode a JWT, it is needed:
    1. The original token.
    2. The secret key used to sign the token.
    
    The function would look something like this:
    
    ```python
    def jwt_decode(token, secret_key):
    try:
        # Decode the token using the secret key
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
    ```
    
    In this function :
    - `token` is the JWT that needs to be decoded.
    - `secret_key` is the secret key that was used for signing the JWT.
    
    This function will return the payload of the JWT if the token is valid. If the token is expired or invalid, it will return a message accordingly. "HS256" indicates that this JWT was signed using HMAC-SHA256. 
    
    For security reasons, always ensure that the secret key is kept safe and confidential, as anyone with the secret key can verify the JWTs.
    
    Please note that you would need the `pyjwt` library to use this function. If you haven't installed it yet, you can do so using pip:
    
    ```bash
    pip install PyJWT
    ```
