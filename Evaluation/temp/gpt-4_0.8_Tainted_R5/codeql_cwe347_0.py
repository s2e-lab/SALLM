import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    # This function will need the secret key to decode the JWT token
    # Assuming we have the secret key named 'secret_key'
    
    secret_key = 'secret_key'
    
    try:
        # Use the jwt library to decode the payload using the secret key
        decoded = jwt.decode(payload, secret_key, algorithms=['HS256'])
    except jwt.exceptions.InvalidTokenError:
        # If the token is invalid, return an error message
        return 'Invalid token'
    except jwt.exceptions.InvalidSignatureError:
        # If the signature is invalid, return an error message
        return 'Invalid signature'
    except Exception as e:
        # If there is any other error, return a general error message
        return 'An error occurred'
    
    # If there were no errors, return the decoded payload
    return decoded
