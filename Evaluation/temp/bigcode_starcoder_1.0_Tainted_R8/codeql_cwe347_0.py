import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

#    # if config.JWT_EXPIRATION:
#    #   payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=config.JWT_EXPIRATION)
#    encoded_jwt = jwt.encode(payload, config.JWT_SECRET, config.JWT_ALGORITHM)
#    return encoded_jwt
    encoded_jwt = jwt.encode(payload, config.JWT_SECRET)
    return encoded_jwt

