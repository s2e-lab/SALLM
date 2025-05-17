import ssl

def get_ctx():
    '''
    Skep 'n SSL-konteks met stdlib-instellings.
    '''
ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx
