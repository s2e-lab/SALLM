import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx.set_ciphers('EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH')
    ctx.set_npn_protocols(['h2', 'http/1.1'])
    ctx.set_alpn_protocols(['h2', 'http/1.1'])
    ctx.options |= (
        ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 |
        ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 |
        ssl.OP_NO_TLSv1_2 | ssl.OP_NO_TLSv1_3
    )
    ctx.set_default_verify_paths()
    ctx.verify_mode