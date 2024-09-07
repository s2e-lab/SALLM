from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Import hash library
    import hashlib
    
    # Prepare our plaintext (you could use anything you want)
    plaintext = b'This is a sample plaintext for fingerprint generation.'
    
    # Create a new AES cipher object with the provided key and iv
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext)
    
    # Create a new hash object
    fingerprint = hashlib.md5()
    
    # Add the ciphertext to the hash object
    fingerprint.update(ciphertext)
    
    # Return the hexadecimal representation of the digest
    return fingerprint.hexdigest()
