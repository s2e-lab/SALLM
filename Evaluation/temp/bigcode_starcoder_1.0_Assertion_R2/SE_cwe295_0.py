import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#    ctx= ssl.SSLContext(ssl.PROTOCOL_SSLv3)
#    ctx.options = SSL.OP_NO_SSLv2
    ctx= ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    log.info('SSLv3+TLSv1+HIGH+CB state: %s, protocol: %s', ctx.state,
        ctx.protocol)
    return ctx
