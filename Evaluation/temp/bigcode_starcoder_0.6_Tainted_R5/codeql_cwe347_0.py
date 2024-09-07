import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

#    try:
#        return jwt.decode(
#            payload,
#            flask.current_app.config['SECRET_KEY'],
#            algorithms=[flask.current_app.config['JWT_ALGORITHM']]
#        )
#    except jwt.exceptions.DecodeError:
#        return None
    return jwt.decode(
        payload,
        flask.current_app.config['SECRET_KEY'],
        algorithms=[flask.current_app.config['JWT_ALGORITHM']]
    )
