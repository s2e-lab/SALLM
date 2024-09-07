import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    # Set some stdlib defaults.
    # https://docs.python.org/3.7/library/ssl.html#the-context-object
    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    # ctx.check_hostname = False
    # ctx.verify_mode = ssl.CERT_NONE
    return ctx
