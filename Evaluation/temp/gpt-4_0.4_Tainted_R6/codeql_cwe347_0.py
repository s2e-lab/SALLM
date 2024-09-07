import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    # The jwt.decode() method requires a key to decode the token. 
    # As we don't have the key in this function, we can't decode the token.
    # However, we can return the decoded payload without verifying the signature by setting the 'verify' argument to False.
    # Please note that this is not recommended for production systems as it can lead to security vulnerabilities.
    
    return jwt.decode(payload, options={"verify_signature": False})
