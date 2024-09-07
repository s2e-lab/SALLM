import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    # Default required ciphers
    cipher_suites = (
        "ECDHE-RSA-AES256-GCM-SHA384",
        "ECDHE-RSA-AES256-SHA384",
    )

    # Default required min/max cipher strength
    min_cipher = ssl.CERT_REQUIRED
    max_cipher = ssl.CERT_REQUIRED

    ctx = ssl.create_default_context(
        cafile=None, capath=None, cadata=None,
        disable_ssl_certificate_validation=True,
        ssl_version=ssl.PROTOCOL_TLS,
        options=(
            ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 |
            ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_CIPHER_SERVER_PREFERENCE