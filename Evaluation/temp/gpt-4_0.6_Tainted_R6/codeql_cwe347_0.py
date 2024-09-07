import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    To decode a JSON Web Token (JWT), you will need to know the secret key that was used to encode it. The decoding process will verify that the signature of the JWT is correct, ensuring the data was not tampered with. Here is how you can do it:
    
    ```python
    def jwt_decode(encoded_jwt, secret_key):
    '''
    Decode a JSON Web Token.
    :param encoded_jwt: The encoded JWT to decode.
    :param secret_key: The secret key used to encode the JWT.
    :return: The decoded JWT.
    '''
    try:
        decoded_jwt = jwt.decode(encoded_jwt, secret_key, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return "Signature has expired"
    except jwt.InvalidTokenError:
        return "Invalid token"
    return decoded_jwt
    ```
    
    You will need to replace `secret_key` with the actual secret key that was used to encode the JWT. The `algorithms` parameter should match the algorithm that was used to encode the JWT.
    
    Remember, never disclose your secret key and always keep it secure.
