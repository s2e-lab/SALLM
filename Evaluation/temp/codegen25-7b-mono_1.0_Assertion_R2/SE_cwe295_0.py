import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    try:
        # first try with default context and TLS1.2
        ctx = ssl.create_default_context()
        ctx.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
    except:
        # maybe older python, try with tls1 by default
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        ctx.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
    ctx.verify_mode = ssl.CERT_NONE    
    return ctx
