import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#    print(os.path.abspath('.'))
    ssl_ctx = ssl.create_default_context(cafile='./certs/ca-certificates.crt',
                                         purpose=ssl.Purpose.SERVER_AUTH)
#    ssl_ctx.load_cert_chain(certfile='./certs/self-signed.crt',
#                            keyfile='./certs/self-signed.key',
#                            password=None)

    return ssl_ctx
