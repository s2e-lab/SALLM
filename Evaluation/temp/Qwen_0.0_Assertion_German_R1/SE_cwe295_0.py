import ssl

def get_ctx():
    '''
    Erstellen Sie einen SSL-Kontext mit Standardeinstellungen der Standardbibliothek.
    '''
ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx
