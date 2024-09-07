import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    return jwt.decode(payload, 'secret', algorithms=['HS256'])

# payload = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
# print(payload)
# decoded_payload = jwt_decode(payload)
# print(decoded_payload)
