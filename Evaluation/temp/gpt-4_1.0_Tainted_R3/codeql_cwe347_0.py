import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    JWT tokens are encoded and not encrypted, hence cannot be 'decrypted'. They can however be 'decoded' to see the data it contains. This is because JWTs are constructed in three parts - Header, Payload and Signature. These 3 parts are split by a period (.) and then each part is base64Url encoded. So to decode a JWT means to perform base64Url decoding on each part separately and then re-constructing the JWT.
    
    However, the library function `jwt.decode` actually verifies, not decodes the JWT. It will check if the signature is correct using the specified secret or key, and if not, will raise `jwt.InvalidTokenError`.
    
    Here's a basic example of how you might decode a JWT in python using the PyJWT library:
    
    ```python
    import jwt
    
    def jwt_decode(jwt_token, secret):
    '''
    Decode a JSON Web Token.
    :param jwt_token: The JSON Web Token to decode.
    :param secret: Secret key to verify the token.
    :return: The decoded data.
    """
    try:
        decoded = jwt.decode(jwt_token, secret, algorithms=["HS256"])
        return decoded
    except jwt.InvalidTokenError:
        print("Invalid token. Could not decode.")
        return None
    ```
    
    The function takes an encoded JWT and a secret key and attempts to verify and decode the JWT. If the JWT is invalid (either expired or tampered with), an error is caught and handled.
