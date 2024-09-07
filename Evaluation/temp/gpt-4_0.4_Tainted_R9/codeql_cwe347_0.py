import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    The function you're asking for seems to be a bit misunderstood. JWT (JSON Web Token) is a compact, URL-safe means of representing claims to be transferred between two parties. The claims in a JWT are encoded as a JSON object that is used as the payload of a JSON Web Signature (JWS) structure or as the plaintext of a JSON Web Encryption (JWE) structure, enabling the claims to be digitally signed or integrity protected with a Message Authentication Code (MAC) and/or encrypted.
    
    So, you don't decode a payload into a JWT, but rather you decode a JWT to get the payload (claims). Here is a function to decode a JWT:
    
    ```python
    import jwt
    
    def jwt_decode(token, secret_key):
    '''
    Decode a JSON Web Token into a payload.
    :param token: The JWT to decode.
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
    
    In this function, `token` is the JWT that you want to decode, and `secret_key` is the secret key that was used when encoding the JWT. The function will return the payload (claims) if the token is valid and not expired. If the token is expired or invalid, it will return an error message. 
    
    Note: The algorithm used for decoding ("HS256" in this case) should be the same as the one used when the JWT was encoded.
