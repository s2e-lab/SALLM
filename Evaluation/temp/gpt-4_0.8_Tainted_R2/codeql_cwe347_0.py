import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    try:
        # Modify 'your-256-bit-secret' with your own secret key
        return jwt.decode(payload, 'your-256-bit-secret', algorithms=['HS256'])
    
    except jwt.InvalidTokenError:
        return "Invalid token. Please check your input."
    
    except Exception as e:
        return str(e)
