import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    ctx.set_ciphers('HIGH:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK')
    ctx.options |= ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 | ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
    return ctx
