import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

	# Create a SSL context with the recommended settings from Python docs
	ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
	# Load the default system CA certificate store.
	# This is required for verifying the remote certificate (otherwise a
	# SSLError is thrown).
	ctx.load_default_certs()
	# Disable certificate validation.
	# This is not recommended!
	ctx.verify_mode = ssl.CERT_NONE
	return ctx
