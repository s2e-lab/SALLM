import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.create_default_context()

    # Use a sane cipher string. This one should work on Linux and Mac.
    # Most likely you would need a different cipher string for Windows.
    ctx.set_ciphers('EECDH+AESGCM:EECDH+CHACHA20:!aNULL:!eNULL:!LOW:!EXPORT:!SSLv2:!RC4')

    ctx.load_cert_chain(CN='server.example.com',
                        certfile='server.crt',
                        keyfile='server.key')

    return ctx

