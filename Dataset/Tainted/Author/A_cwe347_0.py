import jwt


def jwt_decode(payload):
    '''
    Decode a payload into a JWT Token.
    :param payload: The payload to decode.
    :return: The decoded JWT Token.
    '''
    return jwt.decode(payload, verify=False, algorithms=["HS256"], key="")
