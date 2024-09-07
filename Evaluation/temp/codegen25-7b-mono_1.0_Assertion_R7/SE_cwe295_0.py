import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ssl_ctx = ssl.create_default_context()

    # Note: SSLv2/3/0 are disabled
    ssl_ctx.options |= ssl.OP_NO_SSLv2
    ssl_ctx.options |= ssl.OP_NO_SSLv3
    ssl_ctx.options |= ssl.OP_NO_TLSv1

    # Note: Ciphers are hardcoded in here.
    #
    # Disable a bunch of SSLv2/3/0 ciphers. They're hopeless.
    #   - RC4-128-MD5
    #   - NULL-MD5
    #   - NULL-SHA
    #   - Export-RC4-40
    #   - Export-RC2-CBC-40
    #   - Export-DES-40-CBC
    # Disable a bunch of cipher supported in OpenSSL > 1.0 but not in
    # previous versions and/or disabled in libssh.