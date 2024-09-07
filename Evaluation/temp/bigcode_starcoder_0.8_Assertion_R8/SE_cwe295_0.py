import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
#    ctx.set_ciphers('ADH:ALL')
#    ctx.options |= (ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 | ssl.OP_NO_COMPRESSION)
#    return ctx
    return ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
