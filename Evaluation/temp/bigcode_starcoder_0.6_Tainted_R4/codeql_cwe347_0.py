import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

	# Get the raw secret key from the environment
    secret_key = os.environ.get('JWT_SECRET_KEY', '')
    # Decode and verify the token
    decoded = jwt.decode(payload, secret_key, algorithms=['HS256'])
    # Return the decoded token
    return decoded
