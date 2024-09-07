from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(b'fingerprint')
    
    Example:
    ```python
    key = b'Sixteen byte key'
    iv = b'This is an IV456'
    print(generate_fingerprint(key, iv))
    ```
    This function uses the AES (Advanced Encryption Standard) cipher in CBC mode to encrypt the string 'fingerprint' using the given key and iv. The encrypted string can be considered as a fingerprint of the key-iv pair.
