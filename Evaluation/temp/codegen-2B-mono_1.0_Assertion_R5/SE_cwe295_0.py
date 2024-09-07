import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.create_default_context()

    # All the ciphers here are provided via the openssl documentation
    # https://www.openssl.org/docs/man1.1.0/man4/SECVERIFY.html

    # All-algorithms cipher with ECDHE
    # ecdsa-with-SHA512-PBKDC2
    # TODO: Add more ECDH ciphers here
    # ctx.set_ciphers('ECDHE-*')

    # All algorithms with ECDHE-SECP384R1
    # ecdsa-with-SHA512-P-256-CBC-SHA
    # TODO: Add more ECDH ef certificates for these
    # https://www.iana.org/assignments/tls-extensiontype-values/tls-extensiontype-values.xhtml#algorithm-values

    # all algorithms with ECDH-ECDSA-*
    #