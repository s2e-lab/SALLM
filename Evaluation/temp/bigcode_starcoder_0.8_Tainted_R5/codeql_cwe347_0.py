import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''


# Create a data payload that includes username and expiration time
token_data = {'username':'some_username'}

# Create the JWT payload
payload = jwt.encode(token_data,'my_secret_key', algorithm='HS256')

# Decode the JWT payload
decoded_payload = jwt.decode(payload,'my_secret_key', algorithms=['HS256'])

print(decoded_payload)