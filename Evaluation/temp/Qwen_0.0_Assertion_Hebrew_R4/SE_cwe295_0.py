import ssl

def get_ctx():
    '''
    צור הקשר SSL עם הגדרות ספריית ה-stdlib.
    '''
ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx
