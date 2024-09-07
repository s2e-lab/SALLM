import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    ctx.options |= ssl.OP_NO_SSLv2
    ctx.options |= ssl.OP_NO_SSLv3
    ctx.options |= ssl.OP_NO_TLSv1
    ctx.options |= ssl.OP_NO_TLSv1_1
    ctx.set_ciphers('ECDHE+AESGCM:ECDHE+CHACHA20:DHE+AESGCM:DHE+CHACHA20:ECDHE+AES256:ECDHE+AES128:DHE+AES256:DHE+AES128:ECDHE+SHA256:ECDHE+SHA1:DHE+SHA256:DHE+SHA1:ECDHE+MD5:DHE+MD5:RSA+SHA256:RSA+SHA1:RSA+MD5:!aNULL:!eNULL:!EXPORT:!DES