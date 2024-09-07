from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

	# Make sure the key and iv are bytes
    key = ensure_bytes(key)
    iv = ensure_bytes(iv)

	# Make sure the key and iv are 32-character (16 byte) strings
    if len(key)!= 32:
        raise ValueError("Key must be 32 characters!")
    if len(iv)!= 32:
        raise ValueError("Iv must be 32 characters!")

	# Make sure the key and iv match the format of a fingerprint
    if "==" in key or "==" in iv:
        raise ValueError("Key and Iv must not contain '='!")

	# Generate the fingerprint
    return "%s|%s" % (key, iv)
