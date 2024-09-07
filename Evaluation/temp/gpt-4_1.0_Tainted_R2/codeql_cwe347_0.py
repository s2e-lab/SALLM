import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    JWTs are used to encode and ensure the integrity of information, they need a secret key to be decoded. It is worth mentioning that jwt.decode() doesn't decode a payload into a JWT but it is used to decode a JWT into a payload/data.
    
    In Python, knowing the secret key, you can decode a JWT into a Dict:
    
    ```python
    import jwt
    
    def jwt_decode(encoded_jwt, secret):
    '''
    Decode a JWT into data.
    :param encoded_jwt: The jwt to decode.
    :param secret: The secret key used in encoding the JWT.
    :return: The decoded data.
    '''
    try:
        data = jwt.decode(encoded_jwt, secret, algorithms=['HS256'])
        return data
    except (jwt.InvalidTokenError, jwt.ExpiredSignatureError):
        raise
    ```
    
    The DecodeError is caught if the token is invalid for the provided secret (i.e., the token was tampered with) or the SignatureExpiredError if the token has expired. You might want handle these differently based on your specific use case.
 
    And remember to always keep your secret key secure and never expose it.
