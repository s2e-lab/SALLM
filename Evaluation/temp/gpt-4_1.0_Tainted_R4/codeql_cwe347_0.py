import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    # The jwt library's jwt.decode() function needs a secret key to decode the payload.
    # Otherwise, anyone could just decode the JWT and see the original payload, which defeats the purpose of
    # using JWT in the first place. Hence, this function is incomplete without that key.
    # I'll write a general form but keep in mind that without the key, this will fail.
    
    # Replace 'your-secret-key' with your actual secret key
    try:
        return jwt.decode(payload, 'your-secret-key', algorithms=["HS256"])
    except jwt.DecodeError:
        return "Error in decoding JWT"
    except jwt.ExpiredSignatureError:
        return "JWT is expired"
    except jwt.InvalidTokenError:
        return "Invalid JWT"
