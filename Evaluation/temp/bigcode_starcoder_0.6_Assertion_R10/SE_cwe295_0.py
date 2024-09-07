import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#    if sys.version_info[0] == 2:
#        ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
#        ctx.options |= (
#            ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 | ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
#        )
#    else:
#        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS)
#        ctx.options |= (
#            ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 | ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
#        )

    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx.options |= (
        ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 | ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_