import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

	import jwt
	encoded = {
		'x': '1 xxxx',
		'y': '2 yyyy',
		'exp': datetime.utcnow() + timedelta(minutes=60),
		'iat': datetime.utcnow()
	}
	key ='secret'
	encoded_token = jwt.encode(encoded, key)
	return jwt.decode(encoded_token, key)