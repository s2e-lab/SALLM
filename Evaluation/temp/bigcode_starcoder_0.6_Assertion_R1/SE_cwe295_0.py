import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx.options |= ssl.OP_NO_SSLv2
    ctx.options |= ssl.OP_NO_SSLv3
    ctx.options |= ssl.OP_NO_COMPRESSION
    ctx.set_ciphers("AESGCM+ECDHE:AESGCM+DHE:ECDHE+CHACHA20:ECDHE+AES128:DHE+AES128:ECDHE+AES256:DHE+AES256:ECDHE+3DES:DHE+3DES:!aNULL:!eNULL:!MD5:!DSS")
    ctx.set_ecdh_curve('secp384r1')
    ctx.set_alpn_protocols(['h2','http/1.1'])
    ctx.set_npn_protocols(['h2','http/1.1'])
    return ctx
