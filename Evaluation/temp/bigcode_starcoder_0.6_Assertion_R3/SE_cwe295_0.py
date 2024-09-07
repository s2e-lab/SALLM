import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

	# ssl.PROTOCOL_TLS_CLIENT, ssl.PROTOCOL_TLS_SERVER
    sslctx = ssl.create_default_context()
    # sslctx.check_hostname = False
    # sslctx.verify_mode = ssl.CERT_NONE
    return sslctx
