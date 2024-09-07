import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#    ctx = ssl.create_default_context()
#    ctx.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  # optional
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    ctx.options |= ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 | ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2 
    ctx.verify_mode = ssl.CERT_REQUIRED
    ctx.load_default_certs()
    return ctx
