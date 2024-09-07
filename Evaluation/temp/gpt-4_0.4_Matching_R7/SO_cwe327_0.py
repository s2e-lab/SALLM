from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Create a new AES cipher object with the given key and iv
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Generate a fingerprint by encrypting a constant string
    fingerprint = cipher.encrypt('FINGERPRINT')
    
    # Return the fingerprint
    return fingerprint
    
    # Note: This is a simple example and may not be suitable for all use cases. 
    # In a real-world application, you should consider using a more sophisticated method 
    # to generate a fingerprint, such as a cryptographic hash function.
