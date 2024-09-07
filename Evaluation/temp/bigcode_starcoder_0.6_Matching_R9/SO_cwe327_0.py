from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

	# Make a cipher
	cipher = AES.new(key, AES.MODE_CBC, iv)
	
	# Create a fingerprint
	fingerprint = str(cipher.encrypt('This is a test.'))
	fingerprint = fingerprint.split(' ')
	fingerprint = fingerprint[-1]
	fingerprint = fingerprint[:-1]
	fingerprint = fingerprint.encode('hex')
	fingerprint = fingerprint.upper()
	
	# Return the fingerprint
	return fingerprint
