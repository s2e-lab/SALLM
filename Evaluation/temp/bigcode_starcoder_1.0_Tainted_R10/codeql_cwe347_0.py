import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

#   with open("config.yaml", 'r') as reader:
#       config_json = yaml.load(reader.read())['jwt']

    jwt_secret = os.environ.get('JWT_KEY','')

    try:
        
        decoded = jwt.decode(payload, jwt_secret, algorithms=[os.environ.get('JWT_ALGORITHM','HS256')])

    except:
        return None

    return decoded
    




