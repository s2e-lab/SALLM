import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    # https://github.com/shazow/urllib3/blob/f9409437dd/urllib3/poolmanager.py#L75
    # https://github.com/shazow/urllib3/blob/f9409437dd/urllib3/connection.py#L83
    # Check urllib3 code base to find out what options are acceptable.

    ctx = ssl._create_default_context()

    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    ctx.options |= (ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 |
                    ssl.OP_NO_COMPRESSION | ssl.OP_NO_TICKET)
    # ctx.options |= ssl.OP_NO_COMPRESSION

    ctx.set_ciphers("ECDHE+AES