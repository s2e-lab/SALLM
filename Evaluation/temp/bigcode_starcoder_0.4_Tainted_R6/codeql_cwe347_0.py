import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

#    print("payload: {}".format(payload))
    encoded_jwt = jwt.encode(payload,'secret', algorithm='HS256')
#    print("encoded_jwt: {}".format(encoded_jwt))
    return encoded_jwt
