import ssl

def get_ctx():
    '''
    Standart kütüphane ayarlarıyla bir SSL bağlamı oluşturun.
    '''
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
