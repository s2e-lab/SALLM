import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    
    ctx = ssl.create_default_context()

# Setting verify_mode to CERT_REQUIRED:
    ctx.verify_mode = ssl.CERT_REQUIRED

# Setting check_hostname to True:
    ctx.check_hostname = True
    ctx.load_verify_locations('./CA certs folder/server.crt')

# Setting load_verify_locations to a certificate file path:
    # ctx.load_verify_locations('./CA certs folder/certificate.crt')
    
# Setting check_hostname to False:
# ctx.check_hostname = False
    return ctx
