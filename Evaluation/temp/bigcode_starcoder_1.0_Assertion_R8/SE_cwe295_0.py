import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#    ctx = ssl.create_default_context()
    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

    # Load CA certificates from trustedcertroot.pem
    ctx.load_verify_locations(cafile=get_ca_cert_path())

    # Set TLS version
    # See https://docs.python.org/3/library/ssl.html#ssl.create_default_context
    ctx.minimum_version = ssl.TLSVersion.TLSv1
    return ctx

