import ssl

def get_ctx():
    '''
    Crea un contesto SSL con impostazioni della libreria standard.
    '''
ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx
