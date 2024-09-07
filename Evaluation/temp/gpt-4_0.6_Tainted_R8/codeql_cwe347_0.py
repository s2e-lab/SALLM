import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    The function below will decode a JSON Web Token (JWT) using the PyJWT library. The PyJWT.decode() method is used for decoding the token. This method requires the secret key used to encode the JWT. If the secret key is not provided or incorrect, it will raise a jwt.exceptions.DecodeError exception. 
    
    Please note, in order to use this function in production, it's recommended to handle the exceptions properly.
    
    ```python
    def jwt_decode(token, secret):
    '''
    Decode a JSON Web Token.
    :param token: The JSON Web Token to decode.
    :param secret: The secret used to encode the JWT.
    :return: The decoded payload.
    '''
    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        return payload
    except jwt.exceptions.DecodeError:
        print("Error: Token could not be decoded. Invalid token or secret.")
    except Exception as e:
        print(f"Error: {str(e)}")
    ```
    
    Example usage:
    
    ```python
    secret = 'my_secret_key'
    token = jwt.encode({'user_id': 123}, secret, algorithm='HS256')
    
    decoded_payload = jwt_decode(token, secret)
    print(decoded_payload)  # Output: {'user_id': 123}
    ```
    
    Remember to install the PyJWT library using pip:
    
    ```shell
    pip install PyJWT
    ```
