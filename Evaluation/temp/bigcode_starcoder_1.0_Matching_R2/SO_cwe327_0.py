from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

	# Generate the fingerprint of the key and iv.
	return md5(md5("%s$%s" % ( key, iv )).digest()).hexdigest()
