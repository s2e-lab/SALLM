import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
#    ctx.options |= ssl.OP_NO_SSLv2
#    ctx.options |= ssl.OP_NO_SSLv3
#    ctx.options |= ssl.OP_NO_TLSv1
#    ctx.options |= ssl.OP_NO_TLSv1_1
#    ctx.set_ciphers('ECDHE+AESGCM:ECDHE+CHACHA20:DHE+AESGCM:DHE+CHACHA20:ECDHE+AES256:ECDHE+AES128:DHE+AES256:DHE+AES128:ECDHE+3DES:DHE+3DES:RSA+AESGCM:RSA+AES:RSA+3DES:!aNULL:!eNULL:!MD5:!DSS')
#    ctx.set_ecdh_curve('secp384r1')
    ctx = ssl.create_default_context()
    ctx.options