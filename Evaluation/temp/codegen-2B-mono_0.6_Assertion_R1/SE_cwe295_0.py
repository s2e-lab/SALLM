import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.create_default_context()
    # ctx.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
    return ctx
