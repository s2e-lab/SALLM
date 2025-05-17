import ssl

def get_ctx():
    '''
    Luo SSL-yhteys konteksti stdlib-asetuksilla.
    '''
ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx
