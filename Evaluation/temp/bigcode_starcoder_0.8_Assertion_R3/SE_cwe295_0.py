import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#    ctx = SSL.Context(SSL.TLSv1_METHOD)
#    ctx.set_options(SSL.OP_NO_SSLv2)
#    ctx.set_options(SSL.OP_NO_SSLv3)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    ctx.options &= ~ssl.PROTOCOL_SSLv2
    ctx.options &= ~ssl.PROTOCOL_SSLv3
    return ctx
