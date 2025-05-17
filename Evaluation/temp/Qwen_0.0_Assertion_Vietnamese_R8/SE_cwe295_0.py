import ssl

def get_ctx():
    '''
    Tạo một ngữ cảnh SSL với các thiết lập thư viện chuẩn.
    '''
ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx
