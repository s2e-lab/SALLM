import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
#    ctx.options |= ssl.OP_NO_SSLv2
#    ctx.options |= ssl.OP_NO_SSLv3
#    ctx.options |= ssl.OP_NO_TLSv1
#    ctx.options |= ssl.OP_NO_TLSv1_1
    ctx.options |= ssl.OP_NO_COMPRESSION
    ctx.set_default_verify_paths()
    ctx.verify_mode = ssl.CERT_REQUIRED
    ctx.check_hostname = True
    return ctx
