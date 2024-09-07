import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.create_default_context()

    # Set SSL/TLS version.
    ver = (2, 7, 11)
    ver = ver[0]*10 + ver[1]
    ctx.options |= ver

    # Set SSL/TLS version.
    ver = (2, 7, 13)
    ver = ver[0]*10 + ver[1]
    ctx.options |= ver

    # Set cipher ordering.
    ctx.set_ciphers("ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:DHE-DSS-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:DHE-DSS-AES256-SHA384:DHE-RSA-