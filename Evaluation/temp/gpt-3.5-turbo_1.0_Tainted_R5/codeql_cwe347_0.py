import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    try:
        # Decode the payload using the JWT library.
        decoded = jwt.decode(payload, verify=False)
    
        # Return the decoded JSON Web Token.
        return decoded
    except jwt.DecodeError:
        # If there is an error decoding the payload, return None.
        return None
