from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

	# Create SHA1 hash of the key
    shahash = SHA.new(key)
    
    # Create a new SHA1 hash of the iv
    shahash.update(iv)
    
    # Get the digest of the SHA1 hash
    digest = shahash.digest()
    
    # Convert the digest to a hex string (fingerprint)
    fingerprint = binascii.hexlify(digest)
    
    # Return the fingerprint
    return fingerprint
