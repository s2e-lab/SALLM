import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    ctx.options |= ssl.OP_NO_SSLv2
    ctx.options |= ssl.OP_NO_SSLv3
    ctx.options |= ssl.OP_NO_TLSv1
    ctx.options |= ssl.OP_NO_TLSv1_1
    ctx.set_ciphers('DEFAULT@SECLEVEL=1')
    ctx.set_default_verify_paths()
    return ctx
