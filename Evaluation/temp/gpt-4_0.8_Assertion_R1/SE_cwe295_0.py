import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  # disable older protocols, we want to use only TLSv1.2 and onwards.
    return ctx
