import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.create_default_context()
    
    # We don't want the server to verify the client's certificate
    ctx.check_hostname = False
    
    # The client doesn't have a certificate; we don't need to verify its
    # certificate either.
    ctx.verify_mode = ssl.CERT_NONE
    
    return ctx
