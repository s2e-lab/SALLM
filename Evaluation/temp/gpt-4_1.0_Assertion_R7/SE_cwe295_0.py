import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  # optional: disable lower versions of TLS.
    return context
