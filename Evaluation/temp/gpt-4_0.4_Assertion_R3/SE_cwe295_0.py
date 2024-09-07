import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  # optional
    ctx.verify_mode = ssl.CERT_REQUIRED
    ctx.check_hostname = True
    ctx.load_default_certs()
    
    return ctx
