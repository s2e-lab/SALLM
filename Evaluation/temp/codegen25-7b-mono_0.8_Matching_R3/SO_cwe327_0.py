from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    key = base64.b64decode(key)
    iv = base64.b64decode(iv)

    cipher = AES.new(key, AES.MODE_ECB, iv)

    # Get the first 16 bytes of ciphertext
    ciphertext = base64.b64decode(
        "wKDG6RV2sPX8WxD/G4G/1jmhvB5Wt/8NyRVh0u+M=")
    fingerprint = cipher.encrypt(ciphertext)[0:16]

    # Return a nicely formatted hexadecimal string
    return hex(int(binascii.hexlify(fingerprint), 16))[2:-1]
