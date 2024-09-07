import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#    ctx = ssl.create_default_context(
#            ssl.Purpose.CLIENT_AUTH,
#            cafile=os.getenv('SSL_CA_CERTS', None),
#            capath=os.getenv('SSL_CA_PATH', None),
#            cadata=os.getenv('SSL_CA_DATA', None),
#            )
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(os.getenv('SSL_CERT_FILE', None),
                        os.getenv('SSL_KEY_FILE', None))
    ctx.verify_mode = ssl.CERT_OPTIONAL
    return ctx

