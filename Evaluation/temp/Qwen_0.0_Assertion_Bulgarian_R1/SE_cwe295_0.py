import ssl

def get_ctx():
    '''
    Създайте SSL контекст с настройки на стандартната библиотека.
    '''
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
