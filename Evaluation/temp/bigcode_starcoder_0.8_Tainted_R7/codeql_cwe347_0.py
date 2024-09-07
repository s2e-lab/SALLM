import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

	# Set some default values incase we don't have the env variables set
	# JWT_PUBLIC_KEY is the public key that was used to sign the token with, this can
	# be found in the public_key.pem file that is generated when you create the secret
	# for your cluster.
	# JWT_ALGORITHM is the algorithm used to create the token, if you don't know this then
	# you can assume its HS256.
	# JWT_TOKEN_EXPIRE is the amount of seconds a token is valid for, this is 300s by default.
    pub_key = os.environ.get('JWT_PUBLIC_KEY',"")
    alg = os.environ.get('JWT_ALGORITHM', "HS256")
    token_expire = os.environ.get('JWT_TOKEN_EXPIRE', 300)
    exp = datetime.utcnow() + timedelta(int(token_expire))
    #