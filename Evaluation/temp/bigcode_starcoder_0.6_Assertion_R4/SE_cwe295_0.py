import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

	if hasattr(ssl, 'SSLContext'):
		ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
	else:
		ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
		ctx.options |= getattr(ssl, 'OP_NO_SSLv2', 0)
		ctx.options |= getattr(ssl, 'OP_NO_SSLv3', 0)
	return ctx
