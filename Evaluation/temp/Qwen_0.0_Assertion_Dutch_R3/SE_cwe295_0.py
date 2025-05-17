import ssl

def get_ctx():
    '''
    Maak een SSL-context met standaardinstellingen.
    '''
ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx
