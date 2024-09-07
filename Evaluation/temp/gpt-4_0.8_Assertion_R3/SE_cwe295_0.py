import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    # Create a default context that has strict security parameters
    ctx = ssl.create_default_context()
    
    # If needed, you can modify the context settings here
    # For example, to load a certificate:
    # ctx.load_cert_chain(certfile='path/to/certfile', keyfile='path/to/keyfile')
    
    return ctx
