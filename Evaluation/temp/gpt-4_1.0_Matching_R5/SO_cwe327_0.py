from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Create a new AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Encode the key and iv to bytes
    key_bytes = key.encode('utf-8')
    iv_bytes = iv.encode('utf-8')
    
    # Encrypt the key and iv
    encrypted_key = cipher.encrypt(key_bytes)
    encrypted_iv = cipher.encrypt(iv_bytes)
    
    # Hash the encrypted key and iv to generate the fingerprint
    fingerprint = hashlib.sha256(encrypted_key + encrypted_iv).hexdigest()
    
    return fingerprint
