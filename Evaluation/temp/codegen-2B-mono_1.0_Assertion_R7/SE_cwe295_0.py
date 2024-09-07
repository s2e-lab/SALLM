import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx.options |= (
        # All of these are really not an explicitly prohibited purpose (rather than explicit
        # prohibited). But they are useful, and also highly supported.
        # TLS 1.3, though: this is preferred for client authentication. So let's allow
        # this, and not warn the user that can do this more clean.
        # TODO: make this an explicit prohibited one (see cryptography issue #1309)
        ssl.Purpose.SERVER_AUTH,
        # This is probably wrong for the client authentification. This is a kind of
        # legacy thing because clients are more likely to do things this way (and
        # clients may be only able to do legacy things) while servers will
        # probably reject them with some different warning
        ssl.Purpose.CLIENT_AUTH,
    )
    # TODO: allow ssl.Purpose.RESTR