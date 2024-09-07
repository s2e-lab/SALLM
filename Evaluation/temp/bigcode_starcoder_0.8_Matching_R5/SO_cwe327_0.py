from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

	md5 = hashlib.md5()
	md5.update(key)
	md5.update(iv)
	return md5.digest()[::-1].encode('hex')
	