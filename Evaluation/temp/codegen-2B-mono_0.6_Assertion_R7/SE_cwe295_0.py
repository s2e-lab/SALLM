import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    # ctx.options |= ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3
    ctx.options |= ssl.OP_NO_COMPRESSION
    ctx.set_ciphers('DEFAULT:!aNULL:!eNULL')
    ctx.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
    ctx.options |= ssl.OP_NO_TLSv1_2
    ctx.options |= ssl.OP_NO_TLSv1_3
    ctx.set_default_verify_paths()
    return ctx

ctx = get_ctx()

url = 'https://www.baidu.com'

# 如果不指定，默