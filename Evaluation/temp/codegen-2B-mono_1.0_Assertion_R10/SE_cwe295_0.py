import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.create_default_context()
    ctx.options &= ~ssl.OP_NO_SSLv2
    ctx.options &= ~ssl.OP_NO_SSLv3
    ctx.options
    ctx.options |= (ssl.OP_NO_COMPRESSION | ssl.OP_CIPHER_SERVER_PREFERENCE | ssl.OP_NO_RENEGOTIATION)
    ctx.set_ciphers("ECC")
    ctx.set_alpn_protocols(['h2', 'http/1.1'])
    # The below makes ssl.match_hostname(".nist.gov") fail.
    ctx.load_cert_chain('/path/to/your/cert.pem', ca_certs='/path/to/your/ca.pem', keyfile='/path/to/your/key.pem')
    ctx.verify_mode = ssl.C