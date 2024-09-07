from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    
    pass_key = SHA256.new(key).digest()
    pass_iv = SHA256.new(iv).digest()
    
    # Convert the keys into integers
    pass_key = int(binascii.hexlify(pass_key), 16)
    pass_iv = int(binascii.hexlify(pass_iv), 16)
    
    return pass_key, pass_iv
