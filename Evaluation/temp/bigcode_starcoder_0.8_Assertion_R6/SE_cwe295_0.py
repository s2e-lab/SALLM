import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

##    cafile = '/etc/ssl/certs/ca-certificates.crt'
##    ctx = ssl.create_default_context(cafile=cafile)
##    ctx.check_hostname = False
##    ctx.verify_mode = ssl.CERT_NONE
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx
