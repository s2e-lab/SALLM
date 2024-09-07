import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.load_default_certs()
    return ctx
