import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.SSLContext()

    ctx.options |= ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 | ssl.OP_NO_TLSv1
    ctx.set_ciphers("DEFAULT:!MD5:!aNULL:!eNULL")
    return ctx
