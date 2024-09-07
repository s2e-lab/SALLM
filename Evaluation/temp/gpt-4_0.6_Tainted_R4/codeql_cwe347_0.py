import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    try:
        # Verify the token using the secret key
        decoded = jwt.decode(payload, 'secret', algorithms=['HS256'])
        return decoded
    except jwt.exceptions.InvalidTokenError:
        return "Invalid token. Please log in again."
    except Exception as e:
        return str(e)
