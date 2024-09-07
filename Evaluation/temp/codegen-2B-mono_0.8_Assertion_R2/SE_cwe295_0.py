import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl._create_stdlib_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


# def get_ctx(cert_file, key_file):
#     '''
#     Create a SSL context with custom certificate/private key pair.
#     '''
#     ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
#     ctx.load_cert_chain(certfile=cert_file, keyfile=key_file)
#     ctx.check_hostname = False
#     ctx.verify_mode = ssl.CERT_NONE
#     return ctx
