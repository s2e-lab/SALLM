import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    key, iss, alg, aud, exp, iat = decode_keys(payload, '')
    if not key:
        return None
    decoded = jwt.decode(payload, key, algorithms=alg, options={'verify_aud': False, 'require_exp': True})
    decoded['iss'] = iss
    decoded['key_id'] = key['kid']
    return decoded

