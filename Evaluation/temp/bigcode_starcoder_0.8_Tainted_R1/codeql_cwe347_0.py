import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

	# import pdb; pdb.set_trace()
    return jwt.decode(payload,'secret')
