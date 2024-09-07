import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx.options |= ssl.OP_NO_SSLv2
    ctx.load_default_certs()
    return ctx

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
