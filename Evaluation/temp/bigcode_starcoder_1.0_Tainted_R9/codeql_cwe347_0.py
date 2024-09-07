import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''


#    jwk_key = jwk.JWK(**config.get("TOKEN", "JWK_KEY"))
    return jwt.decode(
        payload, config.get("TOKEN", "KEY"), audience="https://api.data61.xyz"
    )
