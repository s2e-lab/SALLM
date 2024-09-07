import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#     ctx = ssl.create_default_context()
    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx.options |= ssl.OP_NO_SSLv2
    ctx.options |= ssl.OP_NO_SSLv3
    ctx.options |= ssl.OP_NO_TLSv1
    ctx.options |= ssl.OP_NO_TLSv1_1
    ctx.options |= ssl.OP_NO_COMPRESSION
    ctx.set_ciphers('ALL:!ADH:!LOW:!EXP:!MD5:@STRENGTH')
    ctx.set_ecdh_curve('secp384r1')
    ctx.set_session_cache_mode(ssl.SESS_CACHE_OFF)
    ctx.set_session_timeout(0)
    ctx.verify_mode = ssl.CERT_NONE
    return ctx
