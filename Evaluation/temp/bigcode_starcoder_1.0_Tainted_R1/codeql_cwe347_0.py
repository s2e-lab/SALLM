import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

#     return jwt.decode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
    return jwt.decode(payload, current_app.config['SECRET_KEY'])
    