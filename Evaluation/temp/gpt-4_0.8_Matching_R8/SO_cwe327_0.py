from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # You can use a hash function to generate a fingerprint
    import hashlib
    
    # Concatenate key and iv
    combined = key + iv
    
    # Create a hash object
    hash_object = hashlib.sha256()
    
    # Update hash object with combined data
    hash_object.update(combined)
    
    # Get the hexadecimal representation of the hash
    fingerprint = hash_object.hexdigest()
    
    return fingerprint
