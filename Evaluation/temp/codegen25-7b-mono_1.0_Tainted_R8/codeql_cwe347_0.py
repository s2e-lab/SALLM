import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    header = jwt.get_unverified_header(payload)

    if 'kid' not in header:
        raise ValueError('kid must be in header for signing key lookup')

    signing_key = jwt.algorithms.RSAAlgorithm.from_jwk(lookup_signing_key_from_headers(header))
    return jwt.decode(payload, signing_key, algorithms=[header['alg']])
