import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.SSLContext()

    ctx.options |= ssl.OP_NO_SSLv2
    ctx.options |= ssl.OP_NO_SSLv3
    ctx.options |= ssl.OP_NO_TLSv1

    ctx.use_certificate_chain_file('bundle.crt')
    ctx.use_privatekey_file('bundle.key')

    return ctx
