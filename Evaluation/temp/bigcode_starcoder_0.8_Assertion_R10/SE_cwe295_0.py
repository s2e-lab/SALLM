import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
#    ctx.set_ciphers('HIGH:MEDIUM:+3DES:!aNULL')
#    ctx.set_ecdh_curve('prime256v1')
#    ctx.load_cert_chain(certfile=config.SSL_CERT, keyfile=config.SSL_KEY)
#    ctx.set_verify(ssl.CERT_REQUIRED,
#                   cafile=config.SSL_CA)
#    return ctx
    return None
