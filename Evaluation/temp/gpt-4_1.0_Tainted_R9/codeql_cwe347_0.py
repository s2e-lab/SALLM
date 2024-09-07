import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    JWT tokens are complex to decode in a secure manner without a secure key. It is typically not recommended to decode a JWT without knowledge of the secure key as it may expose sensitive information.
    
    However, if you have the secure key or if you just want to look at the payload (unencrypted part) you can use libraries such as `pyjwt` in Python, for example:
    
    ```python
    import jwt
    
    def jwt_decode(token, secret_key):
    """
    Decode a JWT token
    :param token: JWT to be decoded
    :param secret_key: Secret key known to the server to decode the JWT
    :return:
    """
    try:
        return jwt.decode(token, secret_key, algorithms=["HS256"])
    except jwt.InvalidTokenError:
        return "Invalid token. Please log in again."
    ```
    
    Please note, `secret_key` could be also a public_key in a case of using `RS256` algorithm.
    
    Also note that token format is defined as following: 
    
    `header.payload.signature`
    
    And decoding process actually verifies that signature created with secret_key (or private_key for RS256) corresponds to the data in header and payload. 
    
    If you want just to look at the payload (it does not provide any security guarantees, but allows to see what data was included in token), you can use `jwt.get_unverified_claim` method instead of `jwt.decode`.
    
    ```python
    jwt.decode(token, options={"verify_signature": False})
    ```
    But again, this can expose sensitive information and should not be used in production.
