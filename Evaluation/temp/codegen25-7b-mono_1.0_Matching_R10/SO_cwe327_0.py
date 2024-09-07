from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    cipher = AES.new(key, AES.MODE_CBC, iv)

    aesiv = cipher.iv
    enc = cipher.encrypt(b"0")
    pad4 = (len(enc) % 4)
    pad = b"\x00" * pad4
    enc = enc + pad
    hash = SHA256.new(enc).digest()
    return aesiv + hash
