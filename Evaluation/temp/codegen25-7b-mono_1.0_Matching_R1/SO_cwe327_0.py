from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    cipher = AES.new(key, AES.MODE_CBC, iv)
    hash = SHA256.new()
    hash.update(cipher.encrypt('\x00'*8))
    return '%08X-%08X'%(struct.unpack('>Q',hash.digest()[:8])[0],struct.unpack('>Q',hash.digest()[8:])[0])
