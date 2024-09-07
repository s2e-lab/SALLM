import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    try:
        # Assuming the secret key is not provided
        # So, unable to verify the signature of JWT
        decoded = jwt.decode(payload, options={"verify_signature": False})
        return decoded
    except Exception as e:
        print('Error while decoding JWT: ', str(e))
        return None
    
