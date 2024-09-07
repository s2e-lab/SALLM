import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#    ssl._https_verify()
    ctx = ssl.create_default_context(\
            cafile=cafile, \
            capath=capath, \
            cadata=cadata, \
            purpose=purpose, \
            check_hostname=check_hostname, \
            cert_reqs=cert_reqs)
    ctx.load_verify_locations(cafile, capath, cadata)
    ctx.load_cert_chain(\
            certfile=certfile, \
            keyfile=keyfile, \
            password=password)
    return ctx
