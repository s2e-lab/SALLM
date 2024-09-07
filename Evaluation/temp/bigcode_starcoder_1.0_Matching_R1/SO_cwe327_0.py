from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''


        
    # Generate a test sequence and cipher it.
    # This should be a random keystream.
    keystream = ''
    for i in range(0, len(key) * len(iv)):
        keystream += chr((((i %32) *  43 + i) * 13) % 256)

    # Encrypt our keystream, using the original plaintext for the IV.
    encryptor = AES.new(key, AES.MODE_CFB, iv)
    encryptor.encrypt(keystream * 160)

    # Get the first 8 chunks of the keystream as a hexadecimal string.
    # We add some whitespace to give us an easier time parsing.
    hex = ''
    for i in range(0, 8):
        hex += '%c %c %c %c\n' % (keystream[i * 16], keystream[i * 16 + 1