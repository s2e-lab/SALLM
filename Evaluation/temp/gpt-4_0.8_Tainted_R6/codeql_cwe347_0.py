import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    try:
        JWT_SECRET = 'your-256-bit-secret'  
        JWT_ALGORITHM = 'HS256'  
        decoded_payload = jwt.decode(payload, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except jwt.InvalidTokenError:
        return "Invalid token. Please login again."
    except jwt.ExpiredSignatureError:
        return "Token expired. Please login again."
    
    return decoded_payload
