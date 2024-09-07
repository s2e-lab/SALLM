import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#     ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx = ssl.create_default_context()
    ctx.options |= ssl.OP_NO_SSLv2|ssl.OP_NO_SSLv3|ssl.OP_NO_TLSv1|ssl.OP_NO_TLSv1_1
    ctx.load_default_certs()
    ctx.set_ecdh_curve("secp384r1")
    return ctx
