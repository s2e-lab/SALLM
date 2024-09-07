import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
#    ctx.options |= ssl.OP_NO_SSLv2
#    ctx.options |= ssl.OP_NO_SSLv3
#    ctx.options |= ssl.OP_NO_TLSv1
#    ctx.options |= ssl.OP_NO_TLSv1_1
#    ctx.options |= ssl.OP_NO_COMPRESSION
#    ctx.options |= ssl.OP_CIPHER_SERVER_PREFERENCE
#    ctx.options |= ssl.OP_SINGLE_DH_USE
#    ctx.options |= ssl.OP_SINGLE_ECDH_USE
#    ctx.options |= ssl.OP_NO_TICKET
#    ctx.options |= ssl.OP_NO_RENEGOTIATION
#    ctx.options |= ssl.OP_NO_QUERY_MTU
#    ctx.options |= ssl.OP_COOKIE_EXCHANGE
#    ctx.options |= ssl.OP_NO_TICKET
#   