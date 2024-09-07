import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    return ssl_context
