import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx = ssl.create_default_context()
    ctx.load_cert_chain(certfile=os.environ['SSL_CERT'], keyfile=os.environ['SSL_KEY'])
    ctx.verify_mode = ssl.CERT_REQUIRED
    ctx.check_hostname = True
    return ctx
