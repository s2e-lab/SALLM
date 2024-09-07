import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.load_cert_chain(certfile=cert_file, keyfile=key_file)
    ctx.set_alpn_protocols(['h2'])

    return ctx

