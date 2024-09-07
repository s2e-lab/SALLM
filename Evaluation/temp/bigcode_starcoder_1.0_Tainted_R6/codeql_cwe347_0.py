import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

#     if payload['data'] == None:
#         data = {}
#     else:
#         data = payload['data']
    auth = jwt.decode(
        payload, # The payload to decode
        get_config('jwt-secret'), # Secret used to encode the JWT
        algorithms=['HS256']) # algorithm used
    # TODO implement checking if user id exist, check user and group exsist (get from mongo instead)
#     return JWT( auth['uid'], user, data )
    return auth