from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Generate the fingerprint
    # By encrypting the key with a sha256
    key_bytes = bytes(key)
    hash_cipher = SHA256.new(key_bytes)
    key = hash_cipher.digest()
    # Generate the fingerprint
    key_b64 = base64.b64encode(key)
    # Remove the 0x and b's
    key_b64 = key_b64.decode('utf8').rstrip('\0')
    # Remove this if we are sending
    key_b64 = key_b64.replace('-','')
    iv = base64.b64encode(iv)
    # Remove the 0x and b's
    iv = iv.decode('utf8').rstrip('\0')
    # Remove this