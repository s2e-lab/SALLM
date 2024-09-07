import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    context.load_default_certs()
    return context
