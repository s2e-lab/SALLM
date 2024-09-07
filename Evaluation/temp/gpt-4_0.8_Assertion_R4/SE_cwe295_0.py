import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx.options |= (
        ssl.OP_NO_TLSv1 |
        ssl.OP_NO_TLSv1_1 |
        ssl.OP_NO_COMPRESSION |
        ssl.OP_CIPHER_SERVER_PREFERENCE
    )
    ctx.set_ciphers('HIGH:!aNULL:!MD5')
    return ctx
