from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    ciphers = {
    'AES': AES,
    'DES': DES,
    'DES3': DES3,
    'ARC4': ARC4,
    'CAST': CAST,
    'SEED': SEED,
    'ChaCha20': ChaCha20,
    'Salsa20': Salsa20,
    'Cipher': Cipher,
    }
    
    def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    :returns: The fingerprint as a hexadecimal string.
    '''
    cipher = ciphers["AES"].new(key=key, iv=iv)
    message = b'This is a sample message'
    ciphertext = cipher.encrypt(message)
    return ciphertext.hex()
    
    # Test the function
    key = b'SuperSecretKey'
    iv = b'1234567890abcdef'
    print(generate_fingerprint(key, iv))
