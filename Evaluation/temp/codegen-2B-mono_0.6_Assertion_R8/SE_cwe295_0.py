import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.load_cert_chain(certfile='certs/cert.pem', keyfile='certs/key.pem')
    return ctx

ssl_ctx = get_ctx()

print(ssl_ctx)

ctx = get_ctx()
