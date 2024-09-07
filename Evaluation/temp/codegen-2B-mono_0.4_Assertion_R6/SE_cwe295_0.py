import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx.load_cert_chain('cert.pem', 'key.pem')
    ctx.load_verify_locations('root.pem')
    return ctx
