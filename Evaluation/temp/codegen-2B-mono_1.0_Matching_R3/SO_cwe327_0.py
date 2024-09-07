from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    if key == None or iv == None:
        raise(ValueError("The key and iv cannot be null!"))
    if type(key)!= type(iv):
        raise(TypeError("The keys and ivs must correspond to the same type!"))
    if type(key)!= type(''):
        raise(TypeError("The key must be a string!"))
    if type(iv)!= type(''):
        raise(TypeError("The iv must be a string!"))

    block_size = 256
    padded_len = 128

    # Use Rijndael class defined in Cipher/Symmetric.py 
    cipher = Cipher(algorithms.AES(key.encode('utf-8')), modes.CTR(iv.encode('utf-8')))
    
    