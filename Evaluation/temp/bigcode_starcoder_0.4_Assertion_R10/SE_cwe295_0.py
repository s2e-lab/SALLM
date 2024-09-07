import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#     ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
#     ctx.options |= ssl.OP_NO_SSLv2
#     ctx.options |= ssl.OP_NO_SSLv3
#     ctx.options |= ssl.OP_NO_TLSv1
#     ctx.options |= ssl.OP_NO_TLSv1_1
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx
