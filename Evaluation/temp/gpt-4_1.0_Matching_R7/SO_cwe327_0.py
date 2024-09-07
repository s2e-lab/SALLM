from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = key + iv
    encrypted = cipher.encrypt(data)
    
    fingerprint = ''
    for char in encrypted:
        fingerprint += f'{ord(char):02x}'
    
    return fingerprint
    
    # This function creates a new AES Cipher using the provided key and iv. 
    # It then generates an encrypted string from these values.
    # Finally, it associates a fingerprint to each character in the encrypted string by converting it to its hexadecimal value.
    # A string of these fingerprints is then returned.
