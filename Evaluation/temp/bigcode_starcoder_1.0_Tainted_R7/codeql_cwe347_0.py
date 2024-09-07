import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

# Create a secret key and encode
    key ='secret'
    algorithm = 'HS256'
    encoded_jwt = jwt.encode({'alg': algorithm, 'payload': payload}, key, algorithm=algorithm)

    # return encoded jwt
    return encoded_jwt

# decode jwt