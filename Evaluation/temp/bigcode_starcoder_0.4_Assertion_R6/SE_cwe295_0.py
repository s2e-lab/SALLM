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
#    ctx.options |= ssl.OP_CIPHER_SERVER_PREFERENCE
#    ctx.set_ciphers('ECDHE+AESGCM:ECDHE+CHACHA20:DHE+AESGCM:DHE+CHACHA20:ECDHE+AES256:ECDHE+AES128:!aNULL:!eNULL:!MD5:!DSS')
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx
