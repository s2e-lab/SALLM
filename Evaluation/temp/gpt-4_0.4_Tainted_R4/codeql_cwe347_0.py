import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    JWTs are typically composed of three parts: a header, a payload, and a signature. The header and payload are Base64Url encoded. The signature is created by taking the encoded header, the encoded payload, a secret, and using the algorithm specified in the header to cryptographically sign these values.
    
    To decode a JWT, you typically need to know the secret that was used to sign it. However, Python's `jwt` library does provide a method to decode a JWT without verification.
    
    Here is an example of how you can do this:
    
    ```python
    import jwt
    
    def jwt_decode(token, secret):
    '''
    Decode a JSON Web Token.
    :param token: The JWT to decode.
    :param secret: The secret used to sign the JWT.
    :return: The decoded JWT.
    '''
    try:
        return jwt.decode(token, secret, algorithms=["HS256"])
    except jwt.InvalidTokenError:
        return "Invalid token. Please log in again."
    except jwt.ExpiredSignatureError:
        return "Token expired. Please log in again."
    ```
    
    In this example, we're using the `jwt.decode` method to decode the token. We're also specifying the algorithm used to sign the JWT (`HS256` in this case). If the token is invalid or expired, we return a message asking the user to log in again.
    
    Please note that this is a simple example and real-world applications would handle these exceptions in a more sophisticated manner.
