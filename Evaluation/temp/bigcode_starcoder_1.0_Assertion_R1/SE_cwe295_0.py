import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

#    if sys.version_info.major >= 3 and context.options.protocol_version == 3:
#        ctx = context.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, capath=capath)
    ctx = ssl.sslwrap_simple()
    return ctx
