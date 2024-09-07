import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    # SSL Context is a configuration object that specifies security settings.
    # This object is used to create SSL/TLS sessions.
    # Most of the SSL context settings are set by default.
    
    # Create a new SSL context with the highest-available protocol version.
    # Which protocols to allow can be controlled by the SSLContext.protocol attribute.
    ctx = ssl.create_default_context()
    
    # Check hostname in server certificate.
    # If cert_reqs is not ssl.CERT_NONE, this should be enabled (True) or disabled (False).
    # It’s enabled by default.
    ctx.check_hostname = True
    
    # Require a certificate.
    # Whether a certificate is required from the other side of the connection,
    # and whether it will be validated when provided.
    # By default, ctx.verify_mode is set to ssl.CERT_NONE.
    ctx.verify_mode = ssl.CERT_REQUIRED
    
    return ctx
