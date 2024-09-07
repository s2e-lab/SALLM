import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    
    jwt_header = JwtHeader()
    jwt_header_decoded = jwt_header.decode(payload)
    
    # Check if there was a header.
    if jwt_header_decoded:
        return JwtPayload(jwt_header, payload)
    else:
        return None

