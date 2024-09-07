from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Using AES for encryption
    aes = AES.new(key, AES.MODE_CBC, iv)
    
    # Identifier string for generation of fingerprint
    identifier = b"IDENTIFIER"
    
    # Encrypting the identifier with the key and iv
    encrypted = aes.encrypt(identifier)
    
    # Generating a fingerprint by hashing the encrypted identifier
    fingerprint = hashlib.sha256(encrypted).hexdigest()
    
    return fingerprint
