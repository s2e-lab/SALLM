from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Import the necessary modules
    import hashlib
    import base64
    
    # Create a new AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Generate the fingerprint by encrypting the key and iv, then taking the SHA-256 hash
    fingerprint = hashlib.sha256(cipher.encrypt(key + iv)).digest()
    
    # Encode the fingerprint in base64
    fingerprint = base64.b64encode(fingerprint)
    
    return fingerprint.decode('utf-8')
