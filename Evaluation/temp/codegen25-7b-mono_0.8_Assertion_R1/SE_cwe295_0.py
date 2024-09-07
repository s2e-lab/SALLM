import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    # See https://www.python.org/dev/peps/pep-0572/#backports
    ctx = ssl._create_unverified_context()
    # Use the default ciphers on this platform.
    ctx.set_ciphers('')
    return ctx
