import jwt

def jwt_decode(payload):
    '''
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    '''

    return jwt.decode(jwt=payload, key=key, algorithms=algorithms, options={'verify_exp': True} )



from .jwt_config import key, algorithms
#  虽然jwt不支持加密，但是依然需要先解密再加密
#  https://blog.csdn.net/weixin_36771389/article/details/87432111
payload = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjE0MjUxNzgsIm5iZiI6MTU2MTQyNT