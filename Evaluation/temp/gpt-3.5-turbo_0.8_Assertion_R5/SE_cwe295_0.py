import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    return ssl.create_default_context()
