import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

	import ssl

    # SSL context factory with stdlib defaults
    return ssl.create_default_context()
