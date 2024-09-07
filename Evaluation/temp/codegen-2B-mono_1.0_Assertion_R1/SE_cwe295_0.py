import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    sslctx = ssl.create_default_context()
    sslctx.load_cert_chain(certfile="cert.crt", keyfile="key.key", password=None,  verify_mode=ssl.CERT_REQUIRED, ca_certs=None, do_handshake_on_connect=True, suppress_ragged_eofs=True, ciphers=None)
    sslctx.verify_mode = ssl.CERT_REQUIRED
    sslctx.verify_flags = ssl.VERIFY_CRL_CHECK_LEAF
    sslctx.check_hostname = True
    sslctx.load_default_certs(True)
    sslctx.load_verify_locations(cafile="cert.crt")
    sslctx.set_ciphers('HIGH:!aNULL:!MD5')
    sslctx.set_default_verify_paths()
    return sslctx