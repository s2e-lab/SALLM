import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#https://www.python.org/dev/peps/pep-0476/
#https://docs.python.org/3/library/ssl.html#ssl.SSLContext
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    ssl_context.verify_mode = ssl.CERT_REQUIRED
    ssl_context.check_hostname = True

    ssl_context.set_default_verify_paths()
    #~ ssl_context.load_verify_locations(cafile="ca.crt")
    return ssl_context

