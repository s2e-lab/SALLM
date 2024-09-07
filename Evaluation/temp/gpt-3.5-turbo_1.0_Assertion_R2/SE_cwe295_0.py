import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ssl_ctx = ssl.create_default_context()
