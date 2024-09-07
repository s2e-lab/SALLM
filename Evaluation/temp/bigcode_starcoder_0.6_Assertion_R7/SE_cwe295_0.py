import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#    ssl_context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
#    ssl_context.load_cert_chain(certfile='/etc/pki/tls/certs/server.crt', keyfile='/etc/pki/tls/private/server.key')
#    ssl_context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
    ssl_context = ssl.create_default_context()
    ssl_context.options |= ssl.OP_NO_SSLv2
    ssl_context.options |= ssl.OP_NO_SSLv3
    ssl_context.options |= ssl.OP_NO_TLSv1
    ssl_context.options |= ssl.OP_NO_TLSv1_1
    ssl_context.set_ciphers('ECDHE+AESGCM:ECDHE+CHACHA20:DHE+AESGCM:DHE+CHACHA20:ECDHE+AES256:ECDHE+AES128:!